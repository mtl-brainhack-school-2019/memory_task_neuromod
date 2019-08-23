# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:17:16 2019

@author: Francois
"""
import os
#import glob
#import tqdm

import future

#def imPaths():
#    imPathlist = []
#    cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd
#    imPathlist = []#Lists all images full paths
#    for r, d, f in os.walk(cwd):
#        for fileName in f:
#            if '.jpg' in fileName:
#                imPathlist.append(os.path.join(r, fileName))
#    return imPathlist    
#trial1_paths = imPaths()


def imPaths(categName):
    imPathlist = []
    cwd = os.getcwd() #Relative path to the image folder - make sure to have it it your cwd
    categPath = cwd +'\\'+ categName
    for r, d, imName in os.walk(categPath):        
        subcats = os.listdir(categPath)
        for subcatName in subcats:
                subcat_path, im_name = os.path.split(im_path)

        for categName in subcatList:
                
        
    subcatPathlist = []
    imPathlist = []#Lists all images full paths
    for r, d, imName in os.walk(categPath):

#        if '.jpg' in imName:
#            imPathlist.append(os.path.join(r, imName))
for subcat in subcatList:

def getCategPath(categName):
    cwd = os.getcwd()
    categPath = cwd + '\\' + 'categName'
    return categPath
categPath = getCategPath('500_clothing')

def getListOfFiles(categName):
    def getCategPath(categName):
        cwd = os.getcwd()
        categPath = cwd + '\\' + 'categName'
        return categPath
    categPath = getCategPath(categName)
    images = {}
    subcats = []
    for root, dirs, imNames in os.walk(categPath):
        subcatPath, imName = os.path.split(categPath)
        subcatName = os.path.basename(subcatPath)
        subcats.append()
        for subcat in dirs:
            images = [os.path.join(root, subcat)] = []
        images[root] = images
#import os
#
#root_folder = r'C:\Users\Steinar\Google Drive\Kode\Ymse\test\test'
#content = {}
#
#for root, dirs, files in os.walk(root_folder):
#    for subdir in dirs:
#        content[os.path.join(root, subdir)] = []
#           
#    content[root] = files
#
## Print out the content dict    
#for folder, filenames in content.items():
#    print 'Folder: {}'.format(folder)
#    print 'Filenames:'
#    for filename in filenames:
#        print '-> {}'.format(filename)


#    non_empty_dirs = [subcatName for subcatName in subcats if subcatName] # filter out empty lists
#    return [item for subitem in non_empty_dirs for item in subitem] # flatten the list
#getListOfFiles('500_clothing')


#    subcatList = os.listdir(categPath)
#    for subcatName in subcatList:
#    imList = list()

#subcats = [subcatName[1] for subcatName in os.walk(categPath)]
#non_empty_dirs = [subcatName for subcatName in subcats if subcatName] # filter out empty lists
#return [item for subitem in non_empty_dirs for item in subitem] # flatten the list

        # Create full path
        subcatPath = os.path.join(categName, subcatName)
        # If subcatName is a directory then get the list of files in this directory 
        if os.path.isdir(subcatPath):
            imList = imList + getListOfFiles(subcatPath)
        else:
            imList.append(subcatPath)
                
    return imLsit

#list1 = ['500_clothing']
#
#for categ in list1:
#    getListOfFiles(categPath, categ)
#camisoleList = getListOfFiles(categPath, categ)
    

#        for fileName in f:
#            if '.jpg' in fileName:
#                imPathlist.append(os.path.join(r, fileName))
#            else: subcatPathlist.append(os.path.realpath(fileName))
#    return subcatPathlist
#    return imPathlist        
#
#trial1 = imPaths('clothings')
#    images = [f for f in glob.glob(categPath +  "**/**/**/*.jpg", recursive=True)]
#    for im_path in tqdm(images):

    
    
    




