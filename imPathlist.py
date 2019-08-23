# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:46:14 2019

@author: Francois
"""

import os

def filePathlist(maindir):
    filePathlist = []
    for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
        for filename in filenames:
            if '.jpg' in filename:
                filePathlist.append(os.path.join(mainpath, filename))
    return filePathlist

impaths = filePathlist('500_clothing\\500_clothing_camisole')