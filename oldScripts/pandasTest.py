# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:34:46 2019

@author: Francois
"""
import os
import pandas as pd

BASE_DIR = 'images/'
train_folder = BASE_DIR+'train/'
train_annotation = BASE_DIR+'annotated_train_data/'

files_in_train = sorted(os.listdir(train_folder))
files_in_annotated = sorted(os.listdir(train_annotation))

images=[i for i in files_in_train if i in files_in_annotated]

df = pd.DataFrame()
df['images']=[train_folder+str(x) for x in images]
df['labels']=[train_annotation+str(x) for x in images]

pd.to_csv('files_path.csv', header=None)

class Category:
    def __init__(self, maindir): #define category name and its folder name (folder must be in cwd!)
        self.maindir = maindir
    def categCreate(self):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
            return sorted(filePathlist)
        imMatrix = [filePathlist(os.path.join(self.maindir,dirname)) for dirname in os.listdir(self.maindir)]
        return tuple(sorted(imMatrix))
categories = [Category(maindir).categCreate() for maindir in os.listdir(os.getcwd()) if '500_' in maindir]