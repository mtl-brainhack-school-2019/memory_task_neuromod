# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 07:55:28 2019

@author: Francois
"""

import os
import random
from psychopy import core
from psychopy import event
from psychopy import visual

class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            filePathlist = []
            for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
            return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))

#List containing lists (categories and subcategories) of images to draw from evenly for each trial
#TODO: Remove hard coding in next line
categories = [[item for sublist in Category('500_clothing').categCreate() for item in sublist],[item for sublist in Category('500_food').categCreate() for item in sublist], [item for sublist in Category('500_furniture').categCreate() for item in sublist]]

#List of all images regardless of respective subcategories to draw from during invalid stimulus presentation during recall
flat_list = [image for category in categories for image in category]


def randStim(categories, nStim):
    randStim = [random.sample(category, nStim) for category in categories]
    for category in randStim:
        nTrial = [image for category in randStim for image in category]
    return nTrial

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1

def runTask(numTrial):
    win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
    trialCount = 1
    while trialCount <= numTrial:
        nTrial = randStim(categories, 4)
        instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.')
        instructionStart.draw()
        win.flip() 
        event.waitKeys()
        
        stimCount = 1
        while stimCount <= len(nTrial):
            for image in nTrial:
                stim = visual.ImageStim(win,image = image, color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
                [stim.draw() for image in nTrial]
                win.flip()
                core.wait(2.5)
                stimCount += 1
                
            instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
            instruction1.draw()
            win.flip()
            core.wait(2.5)
            
            if randSign() == 1:
                target = visual.ImageStim(win,nTrial[random.randint(0, len(nTrial)-1)],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
                target.draw()
                win.flip()
                [flat_list.remove(target.image) for target.image in nTrial]
            else:
                distractor = visual.ImageStim(win, flat_list[random.randint(0, len(flat_list)-1)], color=(1,1,1), pos=(0.0,0.0), size=(500,500))
                distractor.draw()
                win.flip()
                flat_list.remove(distractor.image)
            keys = event.waitKeys(keyList=["y", "n"])
            if 'y' in keys:
                instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
                instruction2.draw()
                win.flip()
                keys = event.waitKeys(keyList=["1", "2","3", "4"])

            trialEnd = visual.TextStim(win, text='Answer saved. Get ready for next round!')
            trialEnd.draw()
            win.flip()
            trialCount +=1
            core.wait(2.5)
win.close()        
runTask(2)
