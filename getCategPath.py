# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:27:41 2019

@author: Francois
"""

import os
### WORKS AS INTENDED, but not useful anymore
def getCategPath(categName):
    cwd = os.getcwd()
    categPath = cwd + '\\' + categName
    return categPath
clothingPath = getCategPath('500_clothing')

