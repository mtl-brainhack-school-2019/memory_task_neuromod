# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:36:17 2019

@author: Francois
"""
import os
import random

class Category:
    def __init__(self, name):
        self.name = name
    def categCreate(self,maindir):
        def filePathlist(maindir):
            filePathlist = []
            for mainpath, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                for filename in filenames:
                    if '.jpg' in filename:
                        filePathlist.append(os.path.join(mainpath, filename))
            return filePathlist
        imMatrix = [filePathlist(os.path.join(maindir,dirname)) for dirname in os.listdir(maindir)]
        return imMatrix
    def imSelect(self, nStim):
        for subcateg in imMatrix:
            imSelection = [random.sample(imPath, nStim) for imPath in category]
        return imSelection
#!/usr/bin/python3
clothing = Category('clothing')
clothingSelection = clothing.imSelect(clothing.name, 14)
#imSelection = clothing.imSelect(clothing, 14)

#class Employee:
#   'Common base class for all employees'
#   empCount = 0
#
#   def __init__(self, name, salary):
#      self.name = name
#      self.salary = salary
#      Employee.empCount += 1
#   
#   def displayCount(self):
#     print ("Total Employee %d" % Employee.empCount)
#
#   def displayEmployee(self):
#      print ("Name : ", self.name,  ", Salary: ", self.salary)
#
##This would create first object of Employee class"
#emp1 = Employee("Zara", 2000)
##This would create second object of Employee class"
#emp2 = Employee("Manni", 5000)
#emp1.displayEmployee()
#emp2.displayEmployee()
#print ("Total Employee %d" % Employee.empCount)