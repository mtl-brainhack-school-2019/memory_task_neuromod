# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 04:06:01 2019

@author: Francois
"""
import os
import random
from psychopy import visual


class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return sorted(filePathlist)
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))

   
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial
flat_list = [image for category in categories for image in category]#


#def randStim(categories, nStim):
#    for category in categories:
#        nTrial = [random.sample(subcat, nStim) for subcat in random.sample(category, nStim)]
#        return nTrial
def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1
    
def randStim(categories, nStim):
    for category in categories:
        nTrial = [random.sample(subcat, nStim) for subcat in random.sample(category, nStim)]
        for stim in nTrial:
            [visual.ImageStim(win,image = nTrial[stim.image], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500)) for stim.image in nTrial]
        return nTrial
#win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
