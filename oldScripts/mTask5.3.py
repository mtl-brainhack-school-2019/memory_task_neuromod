# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:18:09 2019

@author: Francois
"""

import os # Import this one 1st if not already in the directory of the task
import pandas as pd
#import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from secrets import choice
from secrets import randbelow
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
    def filePathlist(mainD):
        for mainD, dirnames,filenames in os.walk(os.path.abspath(mainD)):
            filePathlist = [os.path.join(mainD, filename)
                           for filename in filenames if '.jpg' in filename]
        return (sorted(filePathlist))
    #Allows to create a single Categories object
    @classmethod     
    def categCreate(cls,mainD):
        imMatrix = [cls.filePathlist(os.path.join(mainD,dirname))
                   for dirname in os.listdir(mainD)]
        return tuple(imMatrix)
   
#categs = loadCategsAsList()
class Trials(object):
    def __init__(self,numTrial,nStim,*args,**kwargs):
#        super().__init__(**kwargs)
        self.numTrial = numTrial
        self.nStim = nStim
    
    #Creates a list containing all Categories objects (all at once)
    def loadCategsAsList(self):
        categs = [Categories.categCreate(maindir) 
                 for maindir in os.listdir(os.getcwd()) 
                 if maindir.startswith('500_')]
        return categs
    
    def randImage(self):
        categs = self.loadCategsAsList()
        randCateg = randbelow(len(categs)-1)
        randSubcat = randbelow(len(categs[randCateg]))
        randIm = choice(categs[randCateg][randSubcat])
        return randIm
   
    def getStims(self):
        Encodingstims = [[self.randImage() for stim in range(self.nStim)]
                        for trial in range(self.numTrial)]
        
        Distractors = [[self.randImage() for stim in range(self.nStim-2) 
                       if stim not in flatten(self.Encodingstims)]
                       for trial in range(self.numTrial)]
        
        Targets = [choice(Encodingstims[trial]) 
                  for trial in range(self.numTrial)]
        
        imDF = pd.DataFrame.from_dict({'Encodingstims':Encodingstims,'Distractors':Distractors,'Targets':Targets})
        self.trialslist = list(pd.DataFrame.to_dict(self.imDF,orient='index').values())
        return self.trialsList

#        return {'Encoding':Encodingstims,'Distractors':Distractors,'Targets':Targets}
        
#        self.trialdict = {'Encoding':self.Encodingstims,'Distractors':self.Distractors}
#        return trialdict
trialos = Trials(2,4).getStims()
       

        
        self.trialdict = {'Encoding':Encodingstims,'Distractors':Distractors,'Targets':Targets}
        return self.trialdict
    
trialos = Trials(2,4).getStims()
trialstest = Trials(2,4) .getStims()      
   
       
        self.imDF = pd.DataFrame.from_dict({'Encodingstims':Encodingstims,'Distractors':Distractors,'Targets':Targets})
        self.trialslist = list(pd.DataFrame.to_dict(self.imDF,orient='index').values())
        return self.trialsList

trials = data.TrialHandler(Trials(1,4).trialslist, 1, method='sequential')
       
#        self.Encodingstims = [[secrets.choice(self.categories[secrets.randbelow(len(self.categories))][secrets.randbelow(16)])for stim in range(self.nStim)]for trial in range(self.numTrial)]
#
#    def getEncodingStims(self):
#        return [[secrets.choice(self.categs[secrets.randbelow(len(self.categs))][secrets.randbelow(16))]
#                    for stim in range(self.nStim)]  
#                    for trial in range(self.numTrial)]          
#        self.EncodingStims = getEncodingStims()



#Randomly generates 1 or -1 (quadrant position)
def randSign():
    if secrets.randbelow(2) == 0:
        return 1
    else:
        return -1

        #stimpos = [(250.0, 250.0),(-250.0, -250.0),(250.0, -250.0),(-250.0, -250.0)] #Possibly replacing randSign()
def encodingphase(win): # Shows stimuli in each trial list in "trials"(also list) 
    instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press space to start.') 
    instructionStart.draw()
    win.flip()
    win.getMovieFrame(buffer='front')
    event.waitKeys(keyList=["space"],clearEvents=False)
    for stim in range(len(trials.trialList[eachTrial]['Encodingstims'])-1):
        stimulus = visual.ImageStim(win,
        image = trials.trialList[eachTrial]['Encodingstims'][stim],
        color=(1,1,1), pos = (randSign()*250, randSign()*250),
        size = (500, 500))
        stimulus.draw()
        win.flip()
        win.getMovieFrame(buffer='front')
        core.wait(1)
                
        def recall(win):
            recall_instruct = "You will be presented a series of images." \
                              "Try remembering if you've seen them earlier"\
                              "If so, at which location on screen?"
            beginning = visual.TextStim(win, recall_instruct)
            beginning.draw()
            win.flip()                                     
            instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
            ansRecMessage = visual.TextStim(win, text='Answer recorded')
            random_insert(trials.trialList[eachTrial]['Distractors'],trials.trialList[eachTrial]['Targets'])
            for recallstim in range(len(trials.trialList[eachTrial]['Distractors'])-1):
                instruction1.draw()
                win.flip()
                win.getMovieFrame(buffer='front')
                core.wait(2.5)
                stimulus = visual.ImageStim(win,trials.trialList[eachTrial]['Distractors'][recallstim],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
                stimulus.draw()
                win.flip()
                win.getMovieFrame(buffer='front')
                keys = event.waitKeys(keyList=['y','n']) 
                if  "y" in keys:
                    instruction2 = visual.TextStim(win, text='Where have you seen it? Press 0, 1, 2 or 3 to answer')
                    instruction2.draw()
                    win.flip()
                    win.getMovieFrame(buffer='front')
                    keys = event.waitKeys(keyList=["0","1","2","3"])                    
                ansRecMessage.draw()
                win.flip()
                win.getMovieFrame(buffer='front')
                core.wait(1.0)


def runtask(trials):
    win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
    for eachTrial in range(len(trials.trialList)):
        encodingphase(win)
        recall(win)
        eachTrial +=1
    else:
        instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
        instructionEnd.draw()
        win.flip()
        win.getMovieFrame(buffer='front')
        core.wait(2.5)
        win.saveMovieFrames('C:\\Users\\Francois\\GitHub\\ImageTask\\ImageTask.png', codec='libx264', fps=30, clearFrames=False)
        win.close()
#        core.quit #Would this do the trick to exit the window without restarting the kernel?


def main():
  trials = data.TrialHandler(Trials(1,4).trialslist, 1, method='sequential')
  runtask(trials)
  
if __name__ == "__main__":
    main()