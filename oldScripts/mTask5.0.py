# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:34:27 2019

@author: Francois
"""
import os
#import pandas as pd
#import pprint
import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
#from pandas import DataFrame as df
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

def flatten(categories):  # Returns a list containing all items listed in a list of sublists (for any nesting level) on the same level
	return [stim for subcateg in categories for stim in (flatten(subcateg) if (isinstance(subcateg, Sequence) and not isinstance(subcateg, str)) else [subcateg])]

def random_insert(lst, item): # Insert element to random index in a list
        lst.insert(secrets.randbelow(len(lst)+1), item)
        
def randStim(numTrial, nStim, categories):
    trials = [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trial in range(numTrial)]
    return trials
#trials = randStim(4,8,categories)
#class psychopy.data.TrialHandler(trialList, nReps, method='random', dataTypes=None, extraInfo=None, seed=None, originPath=None, name='', autoLog=True)[source]
#trials = randStim(2,8,categories)
#trials = data.TrialHandler(.......)
#for eachTrial in trials:  # automatically stops when done
#    # do stuff
def getDistractors(numTrial, nStim, categories,trials):
    flatlist = flatten(categories)
    stims = flatten(trials)
    distractors = [[secrets.choice(flatlist)for stim in range(nStim-2) if stim not in stims] for trial in range(numTrial)]
    return distractors
#distractors = getDistractors(4,8,categories,trials)

def getTargets(numTrial,trials):
    targets = [[secrets.choice(trials[trial])] for trial in range(numTrial)]
    return flatten(targets)
#targets = getTargets(4,trials)

def getRecallStims(numTrial, nStim, categories,trials, targets, distractors): # Returns a list containig the stimuli that will be shown during the recall phase
    recallStims = [distractors[trial] for trial in range(numTrial)]           # Includes the distractors for each trial and the target (inserted at a random index)
    for trial in range(len(trials)-1):
        random_insert(recallStims[0],targets[0])
        random_insert(recallStims[1],targets[1])
        return recallStims    
#recallStims = getRecallStims(4, 8, categories,trials, targets, distractors)

def randSign():#randomly generates 1 or -1 (quadrant position)
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
            core.wait(1)

def recall(trialCount, numTrial, trials, nStim, distractors, targets, win):
        instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
        ansRecMessage = visual.TextStim(win, text='Answer recorded')
    #    for distractors[trialCount] in distractors:
        random_insert(distractors[trialCount],targets[trialCount])
        score = [[]for trial in range(trialCount-1)]
        stimCount = 0
        while stimCount <= nStim-2: # Shows all stimuli in recallStims for a given trial
            for distractor in range(len(distractors[trialCount]-1)):
                instruction1.draw()
                win.flip()
                core.wait(2.5)
                stimulus = visual.ImageStim(win,distractors[trialCount][stimCount],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
                stimulus.draw()
                win.flip()
                keys = event.waitKeys(keyList=["y", "n"])
                while stimulus.name == targets[trialCount]:
                    if "y" in keys:
                        instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
                        instruction2.draw()
                        win.flip()
                        keys = [event.waitKeys(keyList=["y", "n","1","2","3","4"]) for key in keys]
        #                    if "y" in keys and stimulus.name == targets[trialCount]:
                        if stimulus.pos.tolist() == [-250.0, 250.0] and "1" in keys[stimCount]:
                            score.insert(stimCount,'recogOKpositionOK')
        #                        return
    #                        stimCount +=1
        #                    pprint.pprint('recogOKpositionOK')
                        elif stimulus.pos.tolist() == [250.0, 250.0] and "2" in keys[stimCount]:
                            score.insert(stimCount,'recogOKpositionOK')
        #                        return
    #                        stimCount +=1
        #                    pprint.pprint('recogOKpositionOK')
                        elif stimulus.pos.tolist() == [-250.0, -250.0] and "3" in keys[stimCount]:
                            score.insert(stimCount,'recogOKpositionOK')
        #                        return
    #                        stimCount +=1
        #                    pprint.pprint('recogOKpositionOK')
                        elif stimulus.pos.tolist() == [250.0, 250.0] and "2" in keys[stimCount]:
                            score.insert(stimCount,'recogOKpositionOK')
        #                        return
    #                        stimCount +=1
        #                    pprint.pprint('recogOKpositionOK')
                        else:
                            score.insert(stimCount,'recogOKpositionWrong')
        #                        return
    #                        stimCount +=1
    #                    stimCount+=1
                    else:
                        score.insert(stimCount,'miss')
    #                    stimCount+=1
                else:
                    if "y" in keys:
                        score.insert(stimCount,'FalseAlarm')
        #                    return
                stimCount +=1
            ansRecMessage.draw()
            win.flip()
            core.wait(1.0)
    #def recall(trialCount, numTrial, trials, nStim, distractors, recallStims, targets, win):
    #    instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
    #    ansRecMessage = visual.TextStim(win, text='Answer recorded')
    #    for recallStims[trialCount] in recallStims:
    #        stimCount = 0
    #        while stimCount <= (nStim-2): # Shows all stimuli in recallStims for a given trial
    #            instruction1.draw()
    #            win.flip()
    #            core.wait(2.5)
    #            stimulus = visual.ImageStim(win,recallStims[trialCount][stimCount],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
    #            stimulus.draw()
    #            win.flip()
    #    #        if stimulus.name == targets[trialCount]:
    #    #            target = stimulus.name # target stimulus can appear at any random moment (target's index in recallStims defined randomly in getRecallStims earlier)
    #            keys = event.waitKeys(keyList=["y", "n"])
    #            score = []
    #            if "y" in keys:
    #                instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
    #                instruction2.draw()
    #                win.flip()
    #                keys = [event.waitKeys(keyList=["y", "n","1","2","3","4"]) for key in keys]
    #                if "y" in keys and stimulus.name == targets[trialCount]:
    #                    if stimulus.pos.tolist() == [-250.0, 250.0] and "1" in keys[stimCount]:
    #                        score.insert(stimCount,'recogOKpositionOK')
    #    #                    stimCount +=1
    #    #                    pprint.pprint('recogOKpositionOK')
    #                    elif stimulus.pos.tolist() == [250.0, 250.0] and "2" in keys[stimCount]:
    #                        score.insert(stimCount,'recogOKpositionOK')
    #    #                    stimCount +=1
    #    #                    pprint.pprint('recogOKpositionOK')
    #                    elif stimulus.pos.tolist() == [-250.0, -250.0] and "3" in keys[stimCount]:
    #                        score.insert(stimCount,'recogOKpositionOK')
    #    #                    stimCount +=1
    #    #                    pprint.pprint('recogOKpositionOK')
    #                    elif stimulus.pos.tolist() == [250.0, 250.0] and "2" in keys[stimCount]:
    #                        score.insert(stimCount,'recogOKpositionOK')
    #    #                    stimCount +=1
    #    #                    pprint.pprint('recogOKpositionOK')
    #                    else:
    #                        score.insert(stimCount,'recogOKpositionWrong')
    #                    stimCount +=1
    #                elif "y" in keys and recallStims[trialCount][stimCount] != targets[trialCount]:
    #                    score.insert(stimCount,'recogWrong')
    #    #                stimCount +=1
    #                elif "n" in keys and recallStims[trialCount][stimCount] == targets[trialCount]:
    #                    score.insert(stimCount,'miss')
    #                stimCount +=1
    #            else:
    #                stimCount +=1
    #            pprint.pprint(score)
    #            ansRecMessage.draw()
    #            win.flip()
    #            core.wait(1.0)

def runTask(numTrial, nStim, categories, win):
    trials = randStim(numTrial,nStim,categories)
    distractors = getDistractors(numTrial, nStim, categories,trials)
    targets = getTargets(numTrial,trials)
#    recallStims = getRecallStims(numTrial, nStim, categories,trials, targets, distractors)
    trialCount = 0
    while trialCount <= numTrial-1:
        encoding(trialCount, numTrial, trials, nStim, win)
        recall(trialCount, numTrial, trials, nStim, distractors, targets, win)
#            getScore(trialCount, numTrial, trials, nStim, recallStims, targets)
        trialCount += 1
    else:
        instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
        instructionEnd.draw()
        win.flip()
        core.wait(2.5)
#        return keys
        win.close()
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial
#keys = event.getKeys()
runTask(2, 8, categories, win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix'))
#return keys
