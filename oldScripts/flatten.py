# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:25:58 2019

@author: Francois
"""
import os
import collections
import random
import secrets
from psychopy import core
from psychopy import event
from psychopy import visual
from typing import Sequence
import numpy as np
import PIL
from PIL import Image
class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return tuple(sorted(filePathlist))
        imMatrix = [Image.open(filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir))]
        return tuple(imMatrix)        
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]#List containing lists (categories and subcategories) of images to draw from evenly for each trial

npCateg = np.array(categories)

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
flatlist = flatten(categories)
for photo in categories[0][0]:
    photo = Image.open(categories[0][0])
    
def flatten(categories):
	return [stim for subcateg in categories for stim in (flatten(subcateg) if (isinstance(subcateg, Sequence) and not isinstance(subcateg, str)) else [subcateg])]
flatten(categories)