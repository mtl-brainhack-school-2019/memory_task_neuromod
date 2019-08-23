# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:30:39 2019

@author: Francois
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:25:05 2019

@author: Francois
"""

### WORKS AS INTENDED, DON'T MODIFY
import os

def getpathlist(dirName):
    pathlist = list()
    cwd = os.getcwd()
    dirPath = cwd + '\\' + dirName #Relative path to the image folder - make sure to have it it your cwd
    for root, dirs, file in os.walk(dirPath):
        for fileName in file:
            if '.jpg' in fileName:
                pathlist.append(os.path.join(root, fileName))
    return pathlist    
trial1_paths = getpathlist('500_clothing_tuxedo')
    
    