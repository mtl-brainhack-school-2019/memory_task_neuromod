# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:52:54 2019

@author: Francois
"""

import os

def categ_create(maindir):
    def filepathlist(maindir):
        filepathlist = []
        for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
             for filename in filenames:
                 if '.jpg' in filename:
                     filepathlist.append(os.path.join(maindir,filename))
        return tuple(sorted(filepathlist))
    imMatrix = {filepathlist(os.path.join(maindir,dirname)) for dirname in os.listdir(maindir)}
    return imMatrix
clothing = categ_create('500_clothing')