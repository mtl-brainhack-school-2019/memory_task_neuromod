# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:38:50 2019

@author: Francois
"""

import os
import random
import secrets
from psychopy import core
from psychopy import event
from psychopy import visual

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
#clothes = Category('500_clothing').categCreate()
        
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial

def randStim(numTrials, nStim):
    trials = [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trials in range(numTrials)]
    return (trials)
trials = randStim(2,8)

def randSign():#randomly generates 1 or -1 (quadrant position)
    if secrets.randbelow(2) ==1:
        return 1
    else:
        return -1

def encoding(trials, categories, nStim, win):
    for trial in trials:
        instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.') 
        instructionStart.draw()
        win.flip()
        event.waitKeys()
#        stimCount = 1
        for stim in range(len(trial)):
            stimulus = visual.ImageStim(win,image = trial[stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            [stimulus.draw() for stimulus.image in trial]
            win.flip()
            core.wait(2.5)
#            stimCount += 1
        win.close()
encoding1 = encoding(2,categories,8,win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')) 

def recall(categories, nStim, win):
    instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
    ansRecMessage = visual.TextStim(win, text='Answer recorded')
    
    target = visual.ImageStim(win,secrets.choice(randStim(nStim)),color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))   
    distractor = visual.ImageStim(win, random.choice(flat_list), color=(1,1,1), pos=(0.0,0.0), size=(500,500))
    for stim in range(len(randStim(nStim))):
        instruction1.draw()
        win.flip()
        core.wait(2.5)
        if secrets.choice(randStim(nStim)) != target:
            distractor.image
            distractor.draw()
            win.flip()
            [flat_list.remove(distractor.image) for distractor.image in flat_list]
            #flat_list = [item for sublist in l for item in sublist]
        elif secrets.choice(randStim(nStim)) == target:
            target.image()
            target.draw()
            win.flip()
        keys = event.waitKeys(keyList=["y", "n"])
        if 'y' in keys:
            instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
            instruction2.draw()
            win.flip()
            keys = event.waitKeys(keyList=["1", "2","3", "4"])
        ansRecMessage.draw()
        win.flip()
        core.wait(1.0)
def runTask(numTrial, categories, nStim, win):
    trialCount = 1
    while trialCount <= numTrial:
        encoding(categories, nStim, win)
        recall(categories, nStim, win)
        trialCount += 1
    win.close()
runTask(3, categories, 8, win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix'))