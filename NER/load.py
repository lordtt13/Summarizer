# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:49:58 2019

@author: tanma
"""
import spacy

def init(filename):
    nlp = spacy.load(filename)
    
    return nlp