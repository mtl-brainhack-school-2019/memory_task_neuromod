# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:25:05 2019

@author: Francois
"""
from __future__ import division
import os

def imPaths():
    imPathlist = []
    cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd
    imPathlist = []#Lists all images full paths
    for r, d, f in os.walk(cwd):
        for fileName in f:
            if '.jpg' in fileName:
                imPathlist.append(os.path.join(r, fileName))
    return imPathlist    
trial1_paths = imPaths()

