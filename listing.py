# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:40:03 2019

@author: Francois
"""
import os
def listing(categName):
    entries = []
    categDir = os.path.join(os.getcwd(), categName)
    for entry in os.listdir(categDir):
        if os.path.isfile(os.path.join(categDir, entry)):
            entries.append(entry)
    return entries

#import os
#
## List all subdirectories using os.listdir
#basepath = 'my_directory/'
#for entry in os.listdir(basepath):
#    if os.path.isdir(os.path.join(basepath, entry)):
#        print(entry)

def imPaths(categName):
    imPathlist = []
    categPath = os.path.abspath(categName)
    for categPath, dirnames, filenames in os.walk(os.path.abspath(categName)):
        for fileName in filenames:
            if '.jpg' in fileName:
                imPathlist.append(os.path.join(categPath, fileName))
    return imPathlist