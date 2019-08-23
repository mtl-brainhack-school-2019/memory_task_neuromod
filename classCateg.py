# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:09:54 2019

@author: Francois
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:36:17 2019

@author: Francois
"""
import os
import random

#Creates a class object (a matrix) listing all image paths in a list according to their subcategory
##Each list is also listed in a bigger list corresponding to the broader semantic category
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
            return filePathlist
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return imMatrix
    def imSelect(self, nStim):
        for subcateg in Category:
            [random.sample(filePathlist, nStim) for filePathlist in subcateg]
        return Category.imSelect(nStim)
clothing = Category('500_clothing').categCreate()
#furniture = Category('500_furniture').categCreate()
