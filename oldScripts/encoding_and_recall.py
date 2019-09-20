# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:30:41 2019

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
clothing = Category('500_clothing').categCreate()

def randStim(categories, nStim):
    for category in categories:
        nTrial = [random.sample(subcat, nStim) for subcat in random.sample(category, nStim)]
        return nTrial

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1
def dice():
    random.randint(1,6)

def encoding(categories, nStim):
    randStim(categories, nStim)
    stimCount = 1
    while stimCount <= len(randStim(categories, nStim)):
        for stim in randStim(categories, nStim):
            stim.image = visual.ImageStim(win,image = randStim(categories, nStim)[stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            [stim.draw() for stim.image in randStim(categories, nStim)]
            win.flip()
            core.wait(2.5)
            stimCount += 1
                
def recall(categories, nStim):
    instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
    trialEnd = visual.TextStim(win, text='Answer saved')
    win.flip()
    core.wait(2.5)
    target = visual.ImageStim(win,random.choice(randStim(categories, nStim)),color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))   
    distractor = visual.ImageStim(win, random.choice(flat_list), color=(1,1,1), pos=(0.0,0.0), size=(500,500))
    for stim in randStim(categories, nStim):
        instruction1.draw()
        if random.randint(1, len(randStim(categories, nStim))) != len(randStim(categories, nStim)):
            distractor.image
            distractor.draw()
            win.flip()
            [flat_list.remove(distractor.image) for distractor.image in flat_list]
            #flat_list = [item for sublist in l for item in sublist]
        elif random.randint(1, len(randStim(categories, nStim))) == len(randStim(categories, nStim)):
            target.image()
            target.draw()
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
            break
        trialEnd.draw()
        win.flip()
        core.wait(1.0)