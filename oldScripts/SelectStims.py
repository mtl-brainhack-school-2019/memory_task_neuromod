# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:30:33 2019

@author: Francois
"""

import os
import secrets
from psychopy import core
from psychopy import event
from psychopy import visual
from typing import Sequence

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
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial

def flatten(irregList):
	return [stim for subcateg in irregList for stim in (flatten(subcateg) if (isinstance(subcateg, Sequence) and not isinstance(subcateg, str)) else [subcateg])]

def randStim(numTrials, nStim, categories):
    return [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trial in range(numTrials)]
trials = randStim(2,8,categories)

def getDistractors(numTrials, nStim, categories,trials):
    flatlist = flatten(categories)
    stims = flatten(trials)
    distractors = [secrets.choice(flatlist)for stim in range(nStim-2) if stim not in stims for trial in range(numTrials)]
    return distractors
distractors = getDistractors(2,8,categories,trials)

def randSign():#randomly generates 1 or -1 (quadrant position)
    if secrets.randbelow(2) == 0:
        return 1
    else:
        return -1