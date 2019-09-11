# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:49:58 2019

@author: tanma
"""
import spacy

def init():
    nlp = spacy.load(r'Final_model')
    
    return nlp