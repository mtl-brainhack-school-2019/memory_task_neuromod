


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

class imStims:
    def __init__(self, imPaths, imSelect):
        def imPaths():
            cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd
            imPaths = []#Lists all images full paths
            for r, d, f in os.walk(cwd):
                for fileName in f:
                    if '.jpg' in fileName:
                        imPaths.append(os.path.join(r, fileName))
            return imPaths
        
        def imSelect(nStim, imPaths):
            imSelect = []
            imCounter = 1
            for item in imPaths:
                while imCounter <= nStim:
                    imSelect.append(imPaths[random.randint(0, len(imPaths))])
                    imCounter +=1
            return imSelect





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
