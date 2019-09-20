# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:59:17 2019

@author: Francois
"""
""" secrets module Generates cryptographically strong random numbers 
     - Prefered to the default pseudo-random number generator in the random module 
     - Uses system's best randomness source (quality depends on system performance)
"""
import os
import pandas as pd
import secrets            
from psychopy import core
from psychopy import event
from psychopy import visual
from typing import Sequence
"""class Category : Creates an image category, a nested tuple of image paths from images in a directory, while keeping the same structure as the directory (as in a file explorer).
    Each index in the tuple ""Category("maindir").categCreate()"" corresponds to a subdirectory, and each subdirectory is a tuple containing all image paths for a given subcategory. 

For example:   'category_name' = Category('maindir').categCreate() : Recursively scans maindir and generates (order as below): 
                path to maindir, list of maindirs's subdirectories names (not paths) as stings, 
                and a list of the filenames at the bottom level of maindir (image paths with extension)
    .categCreate() is a function to initialise the categorizing process. It is necessary to use this method to create an image category.
    This method, with most subsequent functions defined in this script, are destined to sample images in the way inspired by machine learning. 
    By using stings as image (stimuli) paths, images are selected by listing their paths (stings) in the different following sets.
"""
class Category:
    def __init__(self, maindir): # Defines category name and its folder name (folder must be in the current working directory alongside this script!)
        self.maindir = maindir   # import all modules first and run os.chdir('path2yourWorkingDirectory')
    def categCreate(self):
        def filePathlist(maindir): # Lists all images' full paths in alphabetical order in a tuple by joining the the path to each filename to its corresponding filename
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]#Lists all subdirectories' full paths (same as for the images)
        return tuple(imMatrix)        
#categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]
# List containing alphabetically sorted tuples (categories and subcategories) of images to draw from evenly sized directories for each trial

def flatten(categories): # Returns a list containing all items listed in a list of sublists (for any nesting level) on the same level
	return [stim for subcateg in categories for stim in (flatten(subcateg) if (isinstance(subcateg, Sequence) and not isinstance(subcateg, str)) else [subcateg])]

def random_insert(lst, item): # Insert element to random index in a list
        lst.insert(secrets.randbelow(len(lst)+1), item)

def randStim(numTrial, nStim, categories): # Returns a list containing the stimulus lists for each trial, sampled randomly from categories
    trials = [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trial in range(numTrial)]
    return trials
#trials = randStim(2,8,categories)

def getDistractors(numTrial, nStim, categories,trials): # Returns a list containing the distractor lists for each trial 
    flatlist = flatten(categories)                      #(by making sure not to select the same stimuli as listed in trials)
    stims = flatten(trials)
    distractors = [[secrets.choice(flatlist)for stim in range(nStim-2) if stim not in stims] for trial in range(numTrial)]
    return distractors
#distractors = getDistractors(2,8,categories,trials)

def getTargets(numTrial,trials): # Returns a list containing a stimulus (sting) indexed for each trial
    targets = [[secrets.choice(trials[trial])] for trial in range(numTrial)]
    return flatten(targets)
#targets = getTargets(2,trials)

def getRecallStims(numTrial, nStim, categories,trials, targets, distractors): # Returns a list containig the stimuli that will be shown during the recall phase
    recallStims = [distractors[trial] for trial in range(numTrial)]           # Includes the distractors for each trial and the target (inserted at a random index)
    for trial in range(len(trials)-1):
        random_insert(recallStims[0],targets[0])
        random_insert(recallStims[1],targets[1])
        return recallStims    
#recallStims = getRecallStims(2, 8, categories,trials, targets, distractors)

def randSign():#randomly generates 1 or -1 ( used in encoding to determine random position quadrant for each image shown in the experimental window)
    if secrets.randbelow(2) == 0:
        return 1
    else:
        return -1

def encoding(trialCount, numTrial, trials, nStim, win): # Shows stimuli in each trial list in "trials"(also list) 
        instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.') 
        instructionStart.draw()
        win.flip()
        event.waitKeys()
        for stim in range(nStim-1):
            stimulus = visual.ImageStim(win,image = trials[trialCount][stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            stimulus.draw()
            win.flip()
            core.wait(2.5)

def recall(trialCount, numTrial, trials, nStim, distractors, recallStims, targets, win):
    instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
    ansRecMessage = visual.TextStim(win, text='Answer recorded')
    for stim in range(nStim-1):# Shows all stimuli in recallStims for a given trial
        instruction1.draw()
        win.flip()
        core.wait(2.5)
        stimulus = visual.ImageStim(win,recallStims[trialCount][stim],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
        stimulus.draw() # target stimulus can appear at any random moment (target's index in recallStims defined randomly in getRecallStims earlier)
        win.flip()
        recogWrong = []
        recogOKpositionOK = []
        recogOKpositionWrong = []
        keys = event.waitKeys(keyList=["y", "n"])
        if "y" in keys:
            instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
            instruction2.draw()
            win.flip()
            keys = event.waitKeys(keyList=["1", "2","3", "4"])
            if "y" in keys and stimulus.name == targets[trialCount]:
                target = visual.ImageStim(win,targets[trialCount],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
                if target.pos.tolist() == [-250.0, 250.0] and "1" in keys[stim]:
                    recogOKpositionOK.append('recogOKpositionOK')
                elif target.pos.tolist() == [250.0, 250.0] and "2" in keys[stim]:
                    recogOKpositionOK.append('recogOKpositionOK')
                elif target.pos.tolist() == [-250.0, -250.0] and "3" in keys[stim]:
                    recogOKpositionOK.append('recogOKpositionOK')
                elif target.pos.tolist() == [250.0, 250.0] and "2" in keys[stim]:
                    recogOKpositionOK.append('recogOKpositionOK')
                else:
                    recogOKpositionWrong.append('recogOKpositionWrong')
            elif "y" in keys and recallStims[trialCount][stim] != targets[trialCount]:
                recogWrong.append('recogWrong')
        ansRecMessage.draw()
        win.flip()
        core.wait(1.0)
        score = [[recogOKpositionOK], [recogOKpositionWrong], [recogWrong]]
        pd.DataFrame(score)

#def getScore(trialCount, numTrial, trials, nStim, recallStims, targets):
#    target = targets[trialCount]
#    recogOK = []
#    recogOKpositionOK = []
#    recogOKpositionWrong = []
#    recogWrong = []
#    while trialCount <= numTrial:
#        for stim in range(len(recallStims[trialCount])-1):
#            keys = event.getKeys(keyList=["y", "n"],timeStamped=True)
#            if "y" in keys and recallStims[trialCount][stim] == targets[trialCount]:
#                recogOK.append('recogOK')
#            elif "y" in keys and recallStims[trialCount][stim] != targets[trialCount]:
#                recogWrong.append('recogWrong')
#            keys = [[event.getKeys(keyList=["1", "2","3", "4"],timeStamped=True)] for key in keys]
#            positionOK = []
#            if target.pos.tolist() == [-250.0, 250.0] and "1" in keys[stim]:
#                positionOK.append('positionOK')
#            elif target.pos.tolist() == [250.0, 250.0] and "2" in keys[stim]:
#                positionOK.append('positionOK')
#            elif target.pos.tolist() == [-250.0, -250.0] and "3" in keys[stim]:
#                positionOK.append('positionOK')
#            elif target.pos.tolist() == [250.0, 250.0] and "2" in keys[stim]:
#                positionOK.append('positionOK')
#            if positionOK == 1:
#                positionOK.append('positionOK')
#            elif positionOK == 0:
#                recogOKpositionWrong.append('recogOKpositionWrong')
#            score = [[recogOKpositionOK], [recogOKpositionWrong], [recogWrong]]
#            pd.DataFrame(score)

def runTask(numTrial, nStim, categories, win):
    trialCount = 0
    while trialCount == numTrial:
        while trialCount < numTrial:
            trials = randStim(numTrial,nStim,categories)
            distractors = getDistractors(numTrial, nStim, categories,trials)
            targets = getTargets(numTrial,trials)
            recallStims = getRecallStims(numTrial, nStim, categories,trials, targets, distractors)
            for trial in trials[trialCount]:
                encoding(trialCount, numTrial, trials, nStim, win)
                recall(trialCount, numTrial, trials, nStim, distractors, recallStims, targets, win)
    #            getScore(trialCount, numTrial, trials, nStim, recallStims, targets)
                trialCount += 1
        instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
        instructionEnd.draw()
        win.flip()
        win.close()
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial
runTask(2, 8, categories, win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix'))