


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#memory_task
from __future__ import division
import os
from psychopy import core
from psychopy import event
from psychopy import visual #help(visual.ImageStim)
import random

class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            filePathlist = []
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                 for filename in filenames:
                     if '.jpg' in filename:
                         filePathlist.append(os.path.join(maindir,filename))
            return tuple(sorted(filePathlist))
        imMatrix = {filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)}
        return imMatrix

def loadStims(nStim):
    maindirs = os.listdir(os.getcwd())
    categories = [Category(maindir).categCreate() for maindir in maindirs if '500_' in maindir]
    def imSelect(self, nStim):
        for category in categories:
            [random.sample(filePathlist, nStim) for filePathlist in category]
    return categories

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1

win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
class stimList:
        def __init__(self, image, position, keyPressed):
            self.image = image.image
            self.position = image.pos
            self.keyPressed = event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True)
stimCounter = 1
while stimCounter <= nStim:
    image = visual.ImageStim(win,image=imSelect[random.randint(0, nStim-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
    image.draw()
    win.flip()
    core.wait(1.0)
    stimCounter += 1
    key_pressed.append(event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True))
    #stimList.append({'image':image.image, 'position':image.pos})
print(stimList.image, sep = '\n')
win.close()
