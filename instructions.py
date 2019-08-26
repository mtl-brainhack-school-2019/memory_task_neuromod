# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:06:43 2019

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

categories = [[item for sublist in Category('500_clothing').categCreate() for item in sublist],[item for sublist in Category('500_food').categCreate() for item in sublist], [item for sublist in Category('500_furniture').categCreate() for item in sublist]]

def randStim(categories, nStim):
    randStim = [random.sample(category, nStim) for category in categories]
    for category in randStim:
        nTrial = [image for category in randStim for image in category]
    return nTrial
nTrial = randStim(categories, 4)

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1
stimCount = 1

win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.')
instructionStart.draw()
win.flip() 
event.waitKeys()

while stimCount <= len(nTrial):

    for image in nTrial:
        stim = visual.ImageStim(win,image = image, color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
        [stim.draw() for image in nTrial]
        win.flip()
        core.wait(2.5)
        stimCount += 1
win.close()