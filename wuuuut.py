# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:39:55 2019

@author: Francois
"""

import os
import tqdm
import glob


def Category(categName):
    def getCategPath(categName):
        cwd = os.getcwd()
        categPath = cwd + '\\' + categName
        return categPath
    catPath = getCategPath(categName)
    imPathlist = list()
    subcatPathlist = list()
    for categ, subcat, imName in os.walk(catPath):
        images = [f for f in glob.glob(catPath +  "**/**/**/*.jpg", recursive=True)]
        for imPath in tqdm(images):
            subcatPathlist.append()
            subcatPathlist.append(os.path.split(imPath))
            subcatName = list(os.path.basename(subcatPath))
            
            
            
        subcatPathlist.append(os.path.split(catPath))
        for subcatPath in subcatPathlist:
        for fileName in imName:
            if '.jpg' in fileName:
                imPathlist.append(os.path.join(categ, fileName))
    return imPathlist    
clothing = Category('500_clothing')


