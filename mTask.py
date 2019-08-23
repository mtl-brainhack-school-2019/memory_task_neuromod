# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 07:55:28 2019

@author: Francois
"""

import os
import random
from psychopy import visual
from psychopy import core

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
#    randStims = [randStim(categories[0],4), randStim(categories[1],4), randStim(categories[2], 4)]
    for category in randStim:
        trial1 = [image for category in randStim for image in category]
#        trial1 = [image for category in randStim.append(categories[random.randint(0,len(categories))][random.randint(0,len(categories[0]))]) for image in category]
#######################################
    return trial1
trial1 = randStim(categories, 4)
#trial1 = randStim(categories, 5) ##########################
    
win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
   
stimCounter = 1
while stimCounter <= len(randStim(categories, 4))+3:

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
            trial1 = [image for category in randStim for image in category]
        return trial1
    trial1 = randStim(categories, 4)
    
    def randSign():#randomly generates 1 or -1 (quadrant position)
        if random.random() < 0.5:
            return 1
        else:
            return -1
    
    image = visual.ImageStim(win,image=trial1[random.randint(0, len(randStim(categories, 4))-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
    image.draw()
    core.wait(1.0)
    stimCounter += 1
    stimList = []
    stimList.append({'image':image.image, 'position':image.pos})
    win.flip()
win.close()