# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:52:51 2019

@author: Francois
"""
import os

def get_immediate_subdirectories(a_dir):
    if os.path.isdir(os.path.join())
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]