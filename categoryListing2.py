# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:03:10 2019

@author: Francois
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:25:05 2019

@author: Francois
"""

### WORKS AS INTENDED, DON'T MODIFY
import os

def Category(categName):
    def getCategPath(categName):
        cwd = os.getcwd()
        categPath = cwd + '\\' + categName
        return categPath
    category = getCategPath(categName)
    imPathlist = []
    for r, d, f in os.walk(category):
        for fileName in f:
            if '.jpg' in fileName:
                imPathlist.append(os.path.join(r, fileName))
    return imPathlist    
clothing = Category('500_clothing')

