# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 02:16:04 2019

@author: Francois
"""

import os # Import this one 1st if not already in the directory of the task
import pandas as pd
#import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
from pandas import DataFrame as DF
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from secrets import choice
from secrets import randbelow as rb
from typing import Sequence
#from psychopy import logging
#@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@
#logging.console.setLevel(logging.INFO)
# Returns unidimensional list from nested list (any nesting level)
#def flatten(nestedlst):  
#	return [bottomElem for sublist in nestedlst 
#            for bottomElem in (flatten(sublist)
#            if (isinstance(sublist, Sequence)
#            and not isinstance(sublist, str)) else [sublist])
#           ]
def flatten(nestedlst):
    flatten_list = []
    for sublist in nestedlst:
        if not(isinstance(sublist, Sequence)):
            flatten_list.append(sublist)
        else:
            recur_flatten = flatten(sublist)
            flatten_list += recur_flatten
    return flatten_list
    
# Insert element to random index in list
def random_insert(lst, item): 
    return lst.insert(randbelow(len(lst)+1), item)

class Categories(object):
     #Allows to create a single Categories object
    @classmethod
    def filePathlist(cls, maindir):
        for maindir, dirnames,filenames in os.walk(os.path.abspath(maindir)):
            filePathlist = [os.path.join(maindir, filename)
            for filename in filenames if '.jpg' in filename]
            return (sorted(filePathlist))
    #Allows to create a single Categories object
    @classmethod     
    def categCreate(cls,maindir):
        imMatrix = [cls.filePathlist(os.path.join(maindir,dirname))
        for dirname in os.listdir(maindir)]
        return tuple(imMatrix)
    
categos = Categories.filepathlist()    
clothesrand = Categories.filePathlist().randIm()

#categs = [Categories.categCreate(maindir) 
#         for maindir in os.listdir(os.getcwd()) 
#         if maindir.startswith('500_')] 
#categs = loadCategsAsList()
        
randclothing = Categories.categCreate('500_clothing').randIm()
class Trials(object):
    def __init__(self,numTrial,nStim,*args,**kwargs):
#        super().__init__(**kwargs)
        self.numTrial = numTrial
        self.nStim = nStim
        self.categs = [Categories.categCreate(maindir) 
                      for maindir in os.listdir(os.getcwd()) 
                      if maindir.startswith('500_')]

    def randIm(self):
        randCateg = rb(len(self.categs)-1)
        randSubcat = rb(len(self.categs[randCateg]))
        randIm = choice(self.categs[randCateg][randSubcat])
        return randImage
    
    def getStims(self):
        self.Encodingstims = [[self.randIm() for stim in range(self.nStim)]
                             for trial in range(self.numTrial)]
        
        self.Distractors = [[self.randIm() for stim in range(self.nStim-2) 
                           if stim not in flatten(self.Encodingstims)]
                           for trial in range(self.numTrial)]
        
        self.Targets = [choice(self.Encodingstims[trial]) 
                       for trial in range(self.numTrial)]
        
        self.imDF = pd.DataFrame.from_dict({'Encodingstims':self.Encodingstims,
                                            'Distractors':self.Distractors,
                                            'Targets':self.Targets})
        self.trialslist = list(
                              pd.DF.to_dict(self.imDF,orient='index').values()
                              )
        return self.trialslist
    
trialos = Trials(2,8).trialslist    
trials = data.TrialHandler(Trials(2,8).trialslist, 1, method='sequential')

#    def randImage(self):
#        randCateg = rb(len(self.categs)-1)
#        randSubcat = rb(len(self.categs[randCateg]))
#        randIm = choice(self.categs[randCateg][randSubcat])
#        return randIm


    def getStims(self):
        Encodingstims = [[self.randImage() for stim in range(self.nStim)]
                        for trial in range(self.numTrial)]
#        self.Encodingstims = Encodingstims
        
        Distractors = [[self.randImage() for stim in range(self.nStim-2) 
                      if stim not in flatten(Encodingstims)]
                      for trial in range(self.numTrial)]
        self.Distractors = Distractors
        return self.Distractors
        
#        Targets = [choice(Encodingstims[trial]) 
#                  for trial in range(self.numTrial)]
#        self.Targets = Targets
#        return self.__dict__()
#        return (Encodingstims, Distractors, Targets)
#        imDF = pd.DataFrame.from_dict({'Encodingstims':Encodingstims,'Distractors':Distractors,'Targets':Targets})
#        return imDF

trialos = Trials(2,8).getStims()
#      
#        self.trialslist = list(pd.DataFrame.to_dict(imDF,orient='index').values())
#        return self.trialsList

