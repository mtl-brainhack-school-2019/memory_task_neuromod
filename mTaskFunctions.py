# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:00:22 2019

@author: Francois
"""
import os
import random
#from psychopy import visual
#from psychopy import core

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
    
#categories = [[item for sublist in Category('500_clothing').categCreate() for item in sublist],[item for sublist in Category('500_food').categCreate() for item in sublist], [item for sublist in Category('500_furniture').categCreate() for item in sublist]]
    

def randStim(categories, nStim):
    randStim = [random.sample(category, nStim) for category in categories]
#    randStims = [randStim(categories[0],4), randStim(categories[1],4), randStim(categories[2], 4)]
    for category in randStim:
        trial1 = [image for category in randStim for image in category]
        trial1 = [image for category in randStim.append(categories[random.randint(0,len(categories))][random.randint(0,len(categories[0]))]) for image in category]
#######################################
    return trial1
#trial1 = randStim(categories, 4)
#trial1 = randStim(categories, 5) ##########################