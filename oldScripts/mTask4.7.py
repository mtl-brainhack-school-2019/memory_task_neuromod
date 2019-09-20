# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 03:58:06 2019

@author: Francois
"""

import os
from psychopy import core
from psychopy import event
from psychopy import visual
from typing import Sequence
#from pandas import DataFrame as df
import random
import secrets

rng = random.SystemRandom()

class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(imMatrix)        
#categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial

def flatten(categories):
	return [stim for subcateg in categories for stim in (flatten(subcateg) if (isinstance(subcateg, Sequence) and not isinstance(subcateg, str)) else [subcateg])]

def randStim(numTrial, nStim, categories):
    trials = [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trial in range(numTrial)]
    return trials
#trials = randStim(2,8,categories)

def getTargets(numTrial,trials):
    targets = [[secrets.choice(trials[trial])] for trial in range(numTrial)]
    return flatten(targets)
#targets = getTargets(2,trials)

def getDistractors(numTrial, nStim, categories,trials):
    flatlist = flatten(categories)
    stims = flatten(trials)
    distractors = [[secrets.choice(flatlist)for stim in range(nStim-2) if stim not in stims] for trial in range(numTrial)]
    return distractors
#distractors = getDistractors(2,8,categories,trials)

def getRecallStims(numTrial, nStim, categories,trials, targets, distractors):
    recallStims = [distractors[trial] for trial in range(numTrial)]
    for trial in range(numTrial):
        target = targets[trial]
        recallStims[trial].append(target)
        rng.shuffle(recallStims[trial])
        flatten(recallStims[trial])
    return recallStims
#recallStims = getRecallStims(2, 8, categories,trials, targets, distractors)

def randSign():#randomly generates 1 or -1 (quadrant position)
    if secrets.randbelow(2) == 0:
        return 1
    else:
        return -1

def encoding(trialCount, numTrial, trials, nStim, win):
        instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.') 
        instructionStart.draw()
        win.flip()
        event.waitKeys()
        for stim in range(nStim-1):
            stimulus = visual.ImageStim(win,image = trials[trialCount][stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            stimulus.draw()
            win.flip()
            core.wait(2.5)
        
def recall(trialCount, numTrial, trials, nStim, targets, distractors, recallStims, win):
    instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
    ansRecMessage = visual.TextStim(win, text='Answer recorded')
    while trialCount <= numTrial:
        for stim in range(nStim-2):
            instruction1.draw()
            win.flip()
            core.wait(2.5)
            stimulus = visual.ImageStim(win,recallStims[trialCount][stim],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
            stimulus.draw()
            win.flip()
            keys = event.waitKeys(keyList=["y", "n"],timeStamped=True)
            ansRecMessage.draw()
            win.flip()
            core.wait(1)
            if 'y' in keys:
                instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
                instruction2.draw()
                win.flip()
                ansRecMessage.draw()
                win.flip()
                core.wait(1.0)

def getScore(trialCount, numTrial, trials, nStim, targets, recallStims):
    target = targets[trialCount]
    recogOK = []
    recogOKpositionOK = []
    recogOKpositionWrong = []
    recogWrong = []
    while trialCount <= numTrial:
        for stim in range(len(recallStims[trialCount])-1):
            keys = event.getKeys(keyList=["y", "n"],timeStamped=True)
            if "y" in keys and recallStims[trialCount][stim] == targets[target]:
                recogOK.append('recogOK')
            elif "y" in keys and recallStims[trialCount][stim] != targets[target]:
                recogWrong.appemd('recogWrong')
            keys = [[event.getKeys(keyList=["1", "2","3", "4"],timeStamped=True)] for key in keys]
            positionOK = []
            if target.pos.tolist() == [-250.0, 250.0] and "1" in keys[stim]:
                positionOK.append('positionOK')
            elif target.pos.tolist() == [250.0, 250.0] and "2" in keys[stim]:
                positionOK.append('positionOK')
            elif target.pos.tolist() == [-250.0, -250.0] and "3" in keys[stim]:
                positionOK.append('positionOK')
            elif target.pos.tolist() == [250.0, 250.0] and "2" in keys[stim]:
                positionOK.append('positionOK')
            if positionOK == 1:
                positionOK.append('positionOK')
            elif positionOK == 0:
                recogOKpositionWrong.append('recogOKpositionWrong')
            score = [[recogOKpositionOK], [recogOKpositionWrong], [recogWrong]]
            return score

def runTask(numTrial, nStim, categories, win):
    trialCount = 0
    trials = randStim(numTrial,nStim,categories)
    distractors = getDistractors(numTrial, nStim, categories,trials)
    targets = getTargets(numTrial,trials)
    recallStims = recallStims = getRecallStims(2, 8, categories,trials, targets, distractors)
    while trialCount <= numTrial:
        for trial in trials[trialCount]:
            encoding(trialCount, numTrial, trials, nStim, win)
            recall(trialCount, numTrial, trials, nStim, targets, distractors, recallStims, win)
            trialCount +=1
        for trial in trials[trialCount]:
            getScore(trialCount, numTrial, trials, nStim, targets, recallStims)
#        totalScore = [[getScore(trialCount, numTrial, trials, nStim, targets, recallStims)]for trial in trials[trialCount]]
#    return totalScore
#            recall(trialCount, numTrial, trials, nStim, targets, distractors, win)
    win.close()
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial
runTask(2, 8, categories, win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix'))
#score = recogOKpositionOK/(recogOKpositionWrong + recogWrong)
#    score = answers[0]/(answers[1] + answers[2])