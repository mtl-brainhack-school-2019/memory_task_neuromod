# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 02:36:14 2019

@author: Francois
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:18:53 2019

@author: Francois
"""

from __future__ import division
import os


def catCreate(maindir):
    categdict = {}
    def filePathlist(maindir):
        filePathlist = []
        tuple(dirpathlist) = []
        for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
            for dirname in dirnames:
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
    camisole = filePathlist('500_clothing\\500_clothing_camisole')
        return filePathlist
    for categName, subcatNames, imageNames in os.walk(os.path.abspath(maindir)):
        for subcatName in subcatNames:
            subcat = filePathlist(os.path.abspath(os.path.join(categName, subcatName)))
            categdict = dict(zip(tuple(subcatNames),subcat))
    return categdict
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