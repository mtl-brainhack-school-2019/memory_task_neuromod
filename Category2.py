# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:47:30 2019

@author: Francois
"""

import os

def Category(categName): 
    def imPathlist(categName):
        imPathlist = []
        for categPath, dirnames, filenames in os.walk(os.path.abspath(categName)):
            for fileName in filenames:
                if '.jpg' in fileName:
                    imPathlist.append(os.path.join(categPath, fileName))
        return imPathlist
impaths = imPathlist('500_clothing')
    
    
    
    
#    def getCategPath(categName):
#        cwd = os.getcwd()
#        categPath = cwd + '\\' + categName
#        return categPath
#    category = getCategPath(categName)
#    imPathlist = []
#    subcatPathlist = os.listdir(category)
#    for subcat in subcatPathlist:
#        subcat = getCategPath(subcat)
#        for subcatPath in subcatPathlist:
#            for r, d, f in os.walk(subcatPath):
#                for fileName in f:
#                    if '.jpg' in fileName:
#                        imPathlist.append(os.path.join(r, fileName))
#    return imPathlist    
#        
#
#clothing = Category('500_clothing')
#
#
#def imPaths(subcat):
#    def getCategPath(categName):
#        cwd = os.getcwd()
#    categPath = cwd + '\\' + categName
#    return categPath
#    imPathlist = []
#    cwd = os.getcwd()
#    for r, d, f in os.walk(cwd):
#        for fileName in f:
#            if '.jpg' in fileName:
#                imPathlist.append(os.path.join(r, fileName))
#    return imPathlist