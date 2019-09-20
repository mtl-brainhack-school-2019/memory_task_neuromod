# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:32:35 2019

@author: Francois
"""

# Python code to flat a nested list with 
# multiple levels of nesting allowed. 

# input list 
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 

# output list 
output = [] 

# function used for removing nested 
# lists in python. 
def reemovNestings(l): 
	for i in l: 
		if type(i) == list: 
			reemovNestings(i) 
		else: 
			output.append(i) 

# Driver code 
print ('The original list: ', l) 
reemovNestings(l) 
print ('The list after removing nesting: ', output) 

#flat_list = [stim for subcateg in category for stim in subcateg for category in categories]#List of all images regardless of respective subcategories to draw from during invalid stimulus presentation during recall
          #flat_list = [item for sublist in l for item in sublist]
# Python code to flat a nested list with 
# multiple levels of nesting allowed. 
  
# input list 
#l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 
#  
## output list 
#output = [] 
#  
## function used for removing nested  
## lists in python.  
#def reemovNestings(l):
#    flatlist = []
#    for i in l: 
#        if type(i) == tuple: 
#            reemovNestings(i) 
#        else: 
#            flatlist.append(i)
#        return flatlist
## Driver code 
#print ('The original list: ', l) 
#reemovNestings(l) 
#print ('The list after removing nesting: ', output) 
