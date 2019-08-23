# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:23:50 2019

@author: Francois
"""
###Lists all image files in current working directory, then selects a ramdom sample of nStim images from the list to another lsit.
from __future__ import division
import os
import random

#Define target images for each trial

def categCreate(maindir):
    def filePathlist(maindir):
        filePathlist = []
        for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
            for filename in filenames:
                if '.jpg' in filename:
                    filePathlist.append(os.path.join(mainpath, filename))
        return filePathlist
    category = [filePathlist(os.path.join(maindir,dirname)) for dirname in os.listdir(maindir)]
    return category
clothing = categCreate('500_clothing')

def imSelect(category,nStim):
    for subcateg in category:
        imSelection = [random.sample(imPath, nStim) for imPath in category]
    return imSelection
imSelection = imSelect(clothing, 14)