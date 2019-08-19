# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:18:53 2019

@author: Francois
"""

from __future__ import division
import os
import random

class imStims(object):
    def __init__(self, trialNum):
        self.trialNum = trialNum              
    def imSelect(self, nStim):
        imSelection = []
        imCounter = 1
        cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd
        imPaths = []#Lists all images full paths
        for r, d, f in os.walk(cwd):
            for fileName in f:
                if '.jpg' in fileName:
                    imPaths.append(os.path.join(r, fileName)