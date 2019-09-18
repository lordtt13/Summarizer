# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:19:12 2019

@author: tanma
"""

import json

def clean(d):
    new_dict = {}
    for key,value in d.items():
        for i in value:
            x = [i.splitlines() for i in value]
            y = [item for sublist in x for item in sublist]
        new_dict[key] = y
    return new_dict

def main(file_name):
    data = json.load(open(file_name,'r+'))
    data = clean(data)
    json.dump(data,open(file_name,'w+'),indent = 4)