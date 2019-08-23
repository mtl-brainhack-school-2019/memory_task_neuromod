# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:56:31 2019

@author: Francois
"""
import os

def categCreate(maindir):
    def filePathlist(maindir):
        filePathlist = []
        for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
            for filename in filenames:
                if '.jpg' in filename:
                    filePathlist.append(os.path.join(mainpath, filename))
        return filePathlist
    category = [filePathlist(os.path.join(maindir,dirname)) for dirname in os.listdir(maindir)]
    return category
clothing = categCreate('500_clothing')