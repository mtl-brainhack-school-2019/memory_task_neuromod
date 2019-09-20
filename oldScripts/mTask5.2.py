# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:39:42 2019

@author: Francois
"""
import os # Import this one 1st if not already in the directory of the task
import pandas as pd
import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
from psychopy import core
from psychopy import event
from psychopy import visual
from typing import Sequence

def flatten(nestedlst):  # Returns a list containing all items listed in a list of sublists (for any nesting level) on the same level
	return [bottomElem for sublist in nestedlst for bottomElem in (flatten(sublist) if (isinstance(sublist, Sequence) and not isinstance(sublist, str)) else [sublist])]

def random_insert(lst, item): # Insert element to random index in a list 
    return lst.insert(secrets.randbelow(len(lst)+1), item)


#TODO: import image categories as attributes of Categories (for convinience later)
class Categories(object):
    @classmethod #Allows to create a single Categories object
    def categCreate(cls,maindir):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(maindir,dirname)) for dirname in os.listdir(maindir)]
        return tuple(imMatrix)
#        return pd.DataFrame(imMatrix,index=[dirname for dirname in os.listdir(maindir)] ).dropna(how="all")    
    @classmethod #Creates a list containing all Categories objects (all at once)
    def loadCategsAsList(cls):
        categories = [Categories.categCreate(maindir) for maindir in os.listdir(os.getcwd()) if '500_' in maindir]
        return categories
    
"""class Category : Creates an image category, a nested tuple of image paths from images in a directory, while keeping the same structure as the directory (as in a file explorer).
    Each index in the tuple ""Category("maindir").categCreate()"" corresponds to a subdirectory, and each subdirectory is a tuple containing all image paths for a given subcategory. 

For example:   'category_name' = Category('maindir').categCreate() : Recursively scans maindir and generates (order as below): 
                path to maindir, list of maindirs's subdirectories names (not paths) as stings, 
                and a list of the filenames at the bottom level of maindir (image paths with extension)
.categCreate() is a function to initialise the categorizing process. It is necessary to use this method to create an image category.
This method, with most subsequent functions defined in this script, are destined to sample images in the way inspired by machine learning. 
By using stings as image (stimuli) paths, images are selected by listing their paths (stings) in the different following sets.
"""  
# Needs to be run alone first (large amount of data involved)
categories = Categories.loadCategsAsList()

class Trials(object):
    def __init__(self,numTrial,nStim,categories,*args,**kwargs):
#        super().__init__(name, age, sex, city,**kwargs)
        self.numTrial = numTrial
        self.nStim = nStim
        self.categories = categories
        self.Encoding = [[secrets.choice(self.categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(self.nStim)]for trial in range(self.numTrial)]
        self.Distractors = [[secrets.choice(self.categories[secrets.randbelow(len(self.categories))][secrets.randbelow(16)])for stim in range(self.nStim-2) if stim not in flatten(self.Encoding)]for trial in range(self.numTrial)]
        self.Targets = [secrets.choice(self.Encoding[trial]) for trial in range(self.numTrial)]
    def writeTrial(self):
        trialdict = {'Encoding':self.Encoding,'Distractors':self.Distractors,'Targets':self.Targets}
        return pd.DataFrame.from_dict(trialdict)

session1 = Trials(4,8,categories).writeTrial()

def encoding(self, trialCount, numTrial, trials, nStim, win): # Shows stimuli in each trial list in "trials"(also list) 
        def randSign():#randomly generates 1 or -1 (quadrant position)
            if secrets.randbelow(2) == 0:
                return 1
            else:
                return -1    
        instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.') 
        instructionStart.draw()
        win.flip()
        event.waitKeys()
#        for trials[trialCount] in trials:
        for stim in range(nStim-1):
            stimulus = visual.ImageStim(win,image = trials[trialCount][stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            stimulus.draw()
            win.flip()
            core.wait(1)
    #targets = getTargets(4,trials)
    #distractors = getDistractors(4,8,categories,trials)
#        trials = Trials(4,8,categories)   
#    def randStim(self, numTrial, nStim, categories):
#        Trials = [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trial in range(numTrial)]
#        return Trials
#        trials = Trials(4,8,categories)                   
def recall(trialCount, numTrial, trials, nStim, distractors, targets, win):
    instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
    ansRecMessage = visual.TextStim(win, text='Answer recorded')
#    for distractors[trialCount] in distractors:
    random_insert(distractors[trialCount],targets[trialCount])
    stimCount = 0
#    while stimCount <= (nStim-2): # Shows all stimuli in recallStims for a given trial
    score = [[]for trial in range(trialCount-1)]
    while stimCount <= nStim-2:
        for distractor in distractors[trialCount][stimCount]:
            instruction1.draw()
            win.flip()
            core.wait(2.5)
            stimulus = visual.ImageStim(win,distractors[trialCount][stimCount],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
            stimulus.draw()
            win.flip()
            keys = event.waitKeys(keyList=["y", "n"])
            while stimulus.name == targets[trialCount]:
    #                target = stimulus.name # target stimulus can appear at any random moment (target's index in recallStims defined randomly in getRecallStims earlier)
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
    [pd.DataFrame(score[numTrial])for numTrial in range(numTrial-1)]
    trials = randStim(numTrial,nStim,categories)
    distractors = getDistractors(numTrial, nStim, categories,trials)
    targets = getTargets(numTrial,trials)
    trialCount = 0
    while trialCount <= numTrial-1:
        encoding(trialCount, numTrial, trials, nStim, win)
        recall(trialCount, numTrial, trials, nStim, distractors, targets, win)
        trialCount += 1
    else:
        instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
        instructionEnd.draw()
        win.flip()
        core.wait(2.5)
#        return keys
        win.close()
#categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial
runTask(2, 8, categories, win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix'))

#class psychopy.data.TrialHandler(trialList, nReps, method='random', dataTypes=None, extraInfo=None, seed=None, originPath=None, name='', autoLog=True)[source]
#trials = getTrials(2,8,categories)
#trials = data.TrialHandler(.......)
#for eachTrial in trials:  # automatically stops when done
#    # do stuff