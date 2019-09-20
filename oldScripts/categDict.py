# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:16:48 2019

@author: Francois
"""
from flatten_dict import flatten
from functools import reduce
from psychopy import event
from psychopy import core
from psychopy import visual
import os
import pandas as pd
import random
import secrets
rng = random.SystemRandom()
secretsGenerator = secrets.SystemRandom()

def get_directory_structure(rootdir):
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir
clothes = categDict('500_clothing')
categs = {'clothing' : categDict('500_clothing'), 'food' : categDict('500_food')}
cccc = pd.DataFrame(list(categories))
clothing = pd.DataFrame.from_dict(categDict('500_clothing'))
categos = dict.fromkeys(categs,)
categoriesDF = pd.DataFrame.from_dict(categories)
categoriesDF = categoriesDF.transpose()
categoriesExel = categoriesDF.to_excel()

for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)

clothing = categDict('500_clothing')
categs = categDict('categs')
imdf = pd.DataFrame.from_dict(categs)
imdf = imdf.transpose()




#               '500_furniture' : categDict('500_furniture')}
clothingDF = pd.DataFrame.from_dict(categDict('500_clothing'))
categoriesDF = categoriesDF.transpose()
#categoriesDF.dropna(inplace = True) 
imDF = pd.DataFrame.from_dict(categories)
imDF.dropna(inplace = True) 
im_csv = imDF.to_csv()
allflat = pd.DataFrame.from_dict(list(flatten(categories)))
allflat.dropna(inplace = True) 
allflat['imPaths'] = allflat[1].astype(str) + '\\' + allflat[2] + '\\'+ allflat[3]

def randStim(nStim):#Randomly samples nStim images from the DataFrame
    image = random.choice(list(categs.keys()))

    nTrial = [for subcateg in categories[secrets.randbelow(len(categories))],]
    #    nTrial = [secrets.choice(list(allflat['imPaths'])) for stim in range(nStim)]
    return nTrial
#trial = randStim(9)        
def randSign():#randomly generates 1 or -1 (like flipping a coin) for quadrant position
    if random.SystemRandom() < 0.5:
        return 1
    else:
        return -1

def encoding(categories, nStim, win):
    instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press any key to start.') 
    instructionStart.draw()
    win.flip()
    event.waitKeys()
    stimCount = 1
    while stimCount <= nStim:
        for stim in randStim(nStim):
            stim = visual.ImageStim(win,image = os.path.abspath(stim), color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
            [stim.draw() for stim.image in randStim(nStim)]
            win.flip()
            core.wait(2.5)
            stimCount += 1
 
def recall(categories, nStim, win):
    trialEnd = visual.TextStim(win, text='Answer saved')
    target = visual.ImageStim(win,image = secrets.choice(randStim(nStim)),color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))   
    distractor = visual.ImageStim(win, secrets.choice(list(allflat)), color=(1,1,1), pos=(0.0,0.0), size=(500,500))
    for stim in randStim(nStim):
        instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
        instruction1.draw()
        if secrets.choice(range(nStim)) != nStim:
            distractor.image
            distractor.draw()
            win.flip()
            core.wait(2.5)
            [allflat.remove(distractor.image) for distractor.image in allflat]
        elif secrets.choice(range(nStim)) == nStim:
            target.image()
            target.draw()
            win.flip()
        keys = event.waitKeys(keyList=["y", "n"])
    if 'y' in keys:
        instruction2 = visual.TextStim(win, text='Where have you seen it? Press 1,2,3 or 4 to answer')
        instruction2.text
        instruction2.draw()
        win.flip()
        keys = event.waitKeys(keyList=["1", "2","3", "4"])
        trialEnd.draw()
        win.flip()
        core.wait(1.0)
    trialEnd.draw()
    win.flip()
    core.wait(1.0)
    
def runTask(numTrial, categories, nStim, win):  
    trialCount = 1
    while trialCount <= numTrial:
        encoding(categories, nStim, win)
        recall(categories, nStim, win)
        trialCount += 1
    win.close()
runTask(3, categories, 9, win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix'))