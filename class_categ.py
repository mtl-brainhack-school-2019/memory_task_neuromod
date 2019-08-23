# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:28:59 2019

@author: Francois
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:36:17 2019

@author: Francois
"""
import os
import random

class Category:
    def __init__(self, name):
        self.name = name
    def categCreate(self):
        def filePathlist(maindir):
            filePathlist = []
            for mainpath, dirnames, filenames in os.walk(os.path.abspath(self)):
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
            return filePathlist
        category = [filePathlist(os.path.abspath(os.path.join(mainpath,dirname))) for dirname in os.listdir(maindir)]
        return category
    def imSelect(self, nStim):
        for subcateg in self.categCreate():
            imSelection = [random.sample(imPath, nStim) for imPath in subcateg]
        return imSelection
#!/usr/bin/python3
clothing = Category('clothing')
clothing_trial1 = clothing.categCreate()
clothingSelection = clothing_trial1.imSelect(14)