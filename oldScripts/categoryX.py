# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 04:34:57 2019

@author: Francois
"""

import os
import random
from psychopy import core
from psychopy import event
from psychopy import visual

win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')

class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
            return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial
flat_list = [stim for category in categories for stim in category]#List of all images regardless of respective subcategories to draw from during invalid stimulus presentation during recall

def randStim(categories, nStim):
    for category in categories:
        nTrial = [random.sample(subcat, nStim) for subcat in random.sample(category, nStim)]
        return nTrial

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1

def encoding(categories, nStim):
    nTrial = randStim(categories, nStim)
    stimCount = 1
    while stimCount <= len(nTrial):
        for stim in nTrial:
            stim.image = visual.ImageStim(win,image = nTrial[stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            [stim.draw() for stim.image in nTrial]
            win.flip()
            core.wait(2.5)
            stimCount += 1
                
def recall(categories, nStim):
    [instruction1.draw() for visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".') in instruction1.text]
    trialEnd = visual.TextStim(win, text='Answer saved')
    win.flip()
    core.wait(2.5)
    target.image = visual.ImageStim(win,nTrial[random.randint(0,len(nTrial)-1)],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))   
    distractor.image = visual.ImageStim(win, flat_list[random.randint(0, len(flat_list)-1)], color=(1,1,1), pos=(0.0,0.0), size=(500,500))
    if randSign()*randSign() ==1:
        target.draw()
        win.flip()
    elif randSign()*randSign() == -1:
        distractor.image()
        distractor.draw()
        win.flip()
    keys = event.waitKeys(keyList=["y", "n"])
    if 'y' in keys:
        instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
        instruction2.draw()
        win.flip()
        keys = event.waitKeys(keyList=["1", "2","3", "4"])
        trialEnd.draw()
        win.flip()
        core.wait(1.0)
    elif 'n' in keys:
        target.draw()
        trialEnd.draw()
        win.flip()
        core.wait(1.0)
    
def runTask(numTrial, win, nStim):
    trialCount = 1
    while trialCount <= numTrial:
        nTrial = randStim(categories, nStim)
        instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.')
        instructionStart.draw()
        win.flip() 
        event.waitKeys()
        
#        stimCount = 1
#        while stimCount <= len(nTrial):
#            for stim in nTrial:
#                stim.draw()
#                win.flip()
#                core.wait(2.5)
#                stimCount += 1
#                
#            instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
#            instruction1.draw()
#            win.flip()
#            core.wait(2.5)
            
#            target.image = visual.ImageStim(win,nTrial[random.randint(0,len(nTrial)-1)],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))   
#            distractor.image = visual.ImageStim(win, flat_list[random.randint(0, len(flat_list)-1)], color=(1,1,1), pos=(0.0,0.0), size=(500,500))
#            if randSign() == 1:
#                target.draw()
#                win.flip()
#                flat_list.remove(target.image)
#            elif randSign() == -1:
#                distractor.draw()
#                win.flip()
#                flat_list.remove(distractor.image)
#            keys = event.waitKeys(keyList=["y", "n"])
#            trialEnd = visual.TextStim(win, text='Answer saved')
#            if 'y' in keys:
#                instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
#                instruction2.draw()
#                win.flip()
#                keys = event.waitKeys(keyList=["1", "2","3", "4"])
#                trialEnd.draw()
#                win.flip()
#                core.wait(1.0)
#            elif 'n' in keys:
#                trialEnd.draw()
#                win.flip()
#                core.wait(1.0)
        trialCount +=1
    win.close()
runTask(2)