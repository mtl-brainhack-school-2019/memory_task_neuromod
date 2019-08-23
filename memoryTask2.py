# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:45:13 2019

@author: Francois
"""
import os
import random
from psychopy import visual

#Creates a class object (a matrix truple containing lists) all image paths in a list according to their subcategory
##Each list is also listed in a bigger list corresponding to the broader semantic category
class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            filePathlist = []
            for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
            return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))
#clothing = Category('500_clothing').categCreate()


#
#def loadStims():
#    maindirs = os.listdir(os.getcwd())
#    categories = [Category(maindir).categCreate() for maindir in maindirs if '500_' in maindir]
#    for item in categories:
#    return tuple(categories)

categories = [[item for sublist in Category('500_clothing').categCreate() for item in sublist],[item for sublist in Category('500_food').categCreate() for item in sublist], [item for sublist in Category('500_furniture').categCreate() for item in sublist]]


def randStim(categories, nStim):
    randStim = [random.sample(category, nStim) for category in categories]
#    randStims = [randStim(categories[0],4), randStim(categories[1],4), randStim(categories[2], 4)]
    for category in randStim:
        trial1 = [image for category in randStim for image in category]
    return trial1
trial1 = randStim(categories, 4)
#def imSelect(categories, nStim):
#    for category in categories:
#        for imList in subcat:
#            categStims = [random.sample(imList, nStim) for imList in subcat]     
#    return categStims
#flat_list = [item for sublist in l for item in sublist]


#def imSelection(categories, nStim):
#    def imSelect(categories,nStim):
#        for category in categories:
#            for subcateg in category:
#                imSelect = [random.sample(subcateg, nStim) for subcateg in category]
#        return imSelect
#    imSelection = [imSelect(categories, nStim)]
##    imSelection = [subcateg for category in imSelection for category in categories]
#    return imSelection
##    return flatlist
#
#trial1 = imSelection(categories,4)
#trial2 = imSelection(loadStims(),14)

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1

win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            filePathlist = []
            for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
            return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))
#clothing = Category('500_clothing').categCreate()


#
#def loadStims():
#    maindirs = os.listdir(os.getcwd())
#    categories = [Category(maindir).categCreate() for maindir in maindirs if '500_' in maindir]
#    for item in categories:
#    return tuple(categories)

categories = [[item for sublist in Category('500_clothing').categCreate() for item in sublist],[item for sublist in Category('500_food').categCreate() for item in sublist], [item for sublist in Category('500_furniture').categCreate() for item in sublist]]


def randStim(categories, nStim):
    randStim = [random.sample(category, nStim) for category in categories]
#    randStims = [randStim(categories[0],4), randStim(categories[1],4), randStim(categories[2], 4)]
    for category in randStim:
        trial1 = [image for category in randStim for image in category]
    return trial1
trial1 = randStim(categories, 4)
stimCounter = 1
while stimCounter <= len(trial1):
    image = visual.ImageStim(win,image=trial1[random.randint(0, nStim-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
    image.draw()
    win.flip()
    core.wait(1.0)
    stimCounter += 1
    key_pressed.append(event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True))
    #stimList.append({'image':image.image, 'position':image.pos})
print(stimList.image, sep = '\n')
win.close()