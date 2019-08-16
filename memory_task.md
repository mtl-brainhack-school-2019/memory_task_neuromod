{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "# In[ ]:\n",
    "\n",
    "#memory_task\n",
    "from __future__ import division\n",
    "import os\n",
    "from PIL import Image\n",
    "import random\n",
    "from psychopy import core\n",
    "from psychopy import visual\n",
    "from psychopy import event #help(visual.ImageStim)\n",
    "\n",
    "win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')\n",
    "\n",
    "cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd\n",
    "imPaths = []#Lists all images full paths\n",
    "faceCounter = 1\n",
    "for r, d, f in os.walk(cwd):\n",
    "    for fileName in f:\n",
    "        if '.jpg' in fileName:\n",
    "            imPaths.append(os.path.join(r, fileName))\n",
    "            faceCounter += 1           \n",
    "print(imPaths)\n",
    "\n",
    "def randSign():#randomly generates 1 or -1 (quadrant position)\n",
    "    if random.random() < 0.5:\n",
    "        return 1\n",
    "    else:\n",
    "        return -1\n",
    "\n",
    "# CIMA-Q does perfect balancing\n",
    "# Image task images shouldn't be redrawn except for few targets\n",
    "        #define random target variable for each trial?\n",
    "nStim = 15\n",
    "stimCounter = 1\n",
    "stimList = []#List of stimuli used in order with quadrant position for a trial\n",
    "key_pressed = []\n",
    "imageSelection = []\n",
    "imageCounter = 1\n",
    "for item in imPaths:\n",
    "    while imageCounter <= nStim:\n",
    "        imageSelection.append(imPaths[random.randint(0, len(imPaths))])\n",
    "        imageCounter += 1\n",
    "print(*imageSelection, sep = '\\n')\n",
    "\n",
    "while stimCounter <= nStim:\n",
    "    image = visual.ImageStim(win,image=imageSelection[random.randint(0, nStim-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))\n",
    "    image.draw()\n",
    "    win.flip()\n",
    "    core.wait(2.0)\n",
    "    stimCounter += 1\n",
    "    key_pressed.append(event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True))\n",
    "    class stimList:\n",
    "        def __init__(self, image, position, keyPressed):\n",
    "            self.image = image.image\n",
    "            self.position = image.pos\n",
    "            self.keyPressed = event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True)\n",
    "\n",
    "    #stimList.append({'image':image.image, 'position':image.pos})\n",
    "print(*stimList, sep = '\\n')\n",
    "win.close()\n",
    "\n",
    "class stimList:\n",
    "    def __init__(self, image, position, key_pressed):\n",
    "        self.image = image.image\n",
    "        self.position = image.pos\n",
    "        self.key_pressed = event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from __future__ import division\n",
    "import os\n",
    "from PIL import Image\n",
    "import random\n",
    "from psychopy import core\n",
    "from psychopy import visual\n",
    "from psychopy import event #help(visual.ImageStim)\n",
    "image = visual.ImageStim(win,image=imageSelection[random.randint(0, nStim-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#memory_task\n",
    "##importing all necessary packages"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# memory_task\n",
    "## importing all required toolboxes, packages and tools\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
