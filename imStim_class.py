# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:18:53 2019

@author: Francois
"""

from __future__ import division
import os


def catCreate(maindir):
    def filePathlist(maindir):
        filePathlist = []
        for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
            for filename in filenames:
                if '.jpg' in filename:
                    filePathlist.append(os.path.join(mainpath, filename))
        return filePathlist
    for dirname in listdir(maindir):
        if '500_' in dirname:
            
    imList = filePathlist()
#    camisole = filePathlist('500_clothing\\500_clothing_camisole')
    for categdir, subcatNames, imageNames in os.walk(os.path.abspath(maindir)):
        for subcatName in subcatNames:
            subcatNames.insert(len(subcatNames),tuple(filePathlist(categdir)))
            tupsubcatNames = tuple(subcatNames)
            category = dict(zip(maindir,tupsubcatNames))
    return category
clothing = catCreate('500_clothing')

    
#    subcatpathlist  = []
#    for catPath, subcats, imName in os.walk(os.path.abspath(maindir)):
#        for subcat in subcats:
#            subcatpathlist.append(os.path.join(catPath, subcat))
#            for subcatpath in subcatpathlist:
#                imList = filePathlist(subcatpath)
#    return imList

#        

#y = {a : [] for a in range(0,16777216)}
#categ = 
#
#def imPathlist(subcatName):
#    imPathlist = []
#    for categPath, dirnames, filenames in os.walk(os.path.abspath(subcatName)):
#        for fileName in filenames:
#            if '.jpg' in fileName:
#                imPathlist.append(os.path.join(categPath, fileName))
#    return imPathlist
#        named_sims1 = dict(zip(names, sims1))
#print(named_sims1['a'])