# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:46:13 2019

@author: Francois
"""

import os, sys, time
from psychopy import visual, core, data, logging
from .task_base import Task

from ..shared import config
import numpy as np
import os
import pandas as pd
import pprint
import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
#from pandas import DataFrame as df
from psychopy import core
from psychopy import event
from psychopy import visual
from typing import Sequence
STIMULI_DURATION=4
BASELINE_BEGIN=5
BASELINE_END=5
ISI=1
IMAGES_FOLDER = '/home/basile/data/projects/task_stimuli/BOLD5000_Stimuli/Scene_Stimuli/Presented_Stimuli/ImageNet'

STIMULI_SIZE = (400,400)

quadrant_id_to_pos = [
    (-200,100),
    (200,100),
    (-200,-100),
    (200,-100)
]

class ImagePosition(Task):
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        #TODO: image lists as params, subjects ....
        self.item_list = data.importConditions(items_list)
class Categories:
    def __init__(self, maindir): # Defines category name and its folder name (folder must be in the current working directory alongside this script!)
        self.maindir = maindir   # import all modules first and run os.chdir('path2yourWorkingDirectory')
    def categCreate(self):
        def filePathlist(maindir): # Lists all images' full paths in alphabetical order in a tuple by joining the the path to each filename to its corresponding filename
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]#Lists all subdirectories' full paths (same as for the images)
        return pd.DataFrame(imMatrix,index=[os.path.basename(dirname) for dirname in os.listdir(self.maindir)])    
categories = tuple([Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir])
categoriesDF = pd.DateFrame(categories, index = [Category.maindir])
clothingDF.nsmallest()
food = Category('500_food').categCreate()
#categories = np.array(categories)
def flatten(categories):  # Returns a list containing all items listed in a list of sublists (for any nesting level) on the same level
    return [stim for subcateg in categories for stim in (flatten(subcateg) if (isinstance(subcateg, Sequence) and not isinstance(subcateg, str)) else [subcateg])]
#flatarray = np.array(flatten(categories))
def random_insert(lst, item): # Insert element to random index in a list
    lst.insert(secrets.randbelow(len(lst)+1), item)
    
def randStim(numTrial, nStim, categories):
    trials = [[secrets.choice(categories[secrets.randbelow(len(categories))][secrets.randbelow(16)])for stim in range(nStim)]for trial in range(numTrial)]
    return trials
trials = randStim(4,8,clothing)

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
#def getImageSets(numTrial, nStim, categories):
#    trials = randStim(numTrial, nStim, categories)
#    distractors = getDistractors(numTrial, nStim, categories,trials)
#    targets = getTargets(numTrial,trials)
#    recallStims = getRecallStims(numTrial, nStim, categories,trials, targets, distractors)
#    getImageSets = (trials,distractors,targets,recallStims)
#    return imageSets
#imageSets = getImageSets(4, 8, categories)
#imageSetsDF = pd.DataFrame(imageSets,index, columns)
#
#trials = data.TrialHandler(self.item_list, 1, method='sequential')
#img = visual.ImageStim(exp_win,size=STIMULI_SIZE, units='pixels')
#exp_win.logOnFlip(level=logging.EXP,msg='memory: task starting at %f'%time.time())
#for frameN in range(config.FRAME_RATE * BASELINE_BEGIN):
#    yield()
#    for trial in trials:
#        image_path = trial['image_path']
#        img.image = image_path
#        img.pos = quadrant_id_to_pos[trial['quadrant']]
#        exp_win.logOnFlip(level=logging.EXP,msg='memory: display %s in quadrant %d'%(image_path,trial['quadrant']))
#        for frameN in range(config.FRAME_RATE * STIMULI_DURATION):
#            img.draw(exp_win)
#            if ctl_win:
#                img.draw(ctl_win)
#            yield()
#        exp_win.logOnFlip(level=logging.EXP,msg='memory: rest')
#        for frameN in range(config.FRAME_RATE * ISI):
#            yield()
#    for frameN in range(config.FRAME_RATE * BASELINE_END):
#        yield()
#DEFAULT_INSTRUCTION = """You will be presented a set of items in different quadrant of the screen.
#                            Try to remember the items and their location on the screen."""

#def instructions(self, exp_win, ctl_win):
#    screen_text = visual.TextStim(
#        exp_win, text=self.instruction,
#        alignHoriz="center", color = 'white', wrapWidth=config.WRAP_WIDTH)
#
#    for frameN in range(config.FRAME_RATE * config.INSTRUCTION_DURATION):
#        screen_text.draw(exp_win)
#        if ctl_win:
#            screen_text.draw(ctl_win)
#        yield()
#
#def _run(self, exp_win, ctl_win):

categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]
# List containing alphabetically sorted tuples (categories and subcategories) of images to draw from evenly sized directories for each trial



        