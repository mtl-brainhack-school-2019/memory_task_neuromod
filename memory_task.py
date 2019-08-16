


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#memory_task
from __future__ import division
import os
from PIL import Image
from psychopy import core
from psychopy import event
from psychopy import visual #help(visual.ImageStim)
import random


cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd
imPaths = []#Lists all images full paths
faceCounter = 1
for r, d, f in os.walk(cwd):
    for fileName in f:
        if '.jpg' in fileName:
            imPaths.append(os.path.join(r, fileName))
            faceCounter += 1           
print(imPaths)

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1

# CIMA-Q does perfect balancing
# Image task images shouldn't be redrawn except for few targets
        #define random target variable for each trial?
nStim = 15
stimCounter = 1
stimList = []#List of stimuli used in order with quadrant position for a trial
key_pressed = []
imageSelection = []
imageCounter = 1
for item in imPaths:
    while imageCounter <= nStim:
        imageSelection.append(imPaths[random.randint(0, len(imPaths))])
        imageCounter += 1
print(*imageSelection, sep = '\n')

win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
class stimList:
        def __init__(self, image, position, keyPressed):
            self.image = image.image
            self.position = image.pos
            self.keyPressed = event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True)
while stimCounter <= nStim:
    image = visual.ImageStim(win,image=imageSelection[random.randint(0, nStim-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
    image.draw()
    win.flip()
    core.wait(1.0)
    stimCounter += 1
    key_pressed.append(event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True))
    #stimList.append({'image':image.image, 'position':image.pos})
print(stimList.image, sep = '\n')
win.close()

#class stimList:
#    def __init__(self, image, position, key_pressed):
#        self.image = image.image
#        self.position = image.pos
#        self.key_pressed = event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True)
