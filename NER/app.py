# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:46:53 2019

@author: tanma
"""

import main_model as mm
import spacy

text = ''
sample_doc = 'converted.txt'
f = open(sample_doc,'r',encoding = 'utf-8', errors = 'ignore')
for i in f.readlines():
    text += i
text = text[:1000000]
f.close()

nlp = spacy.load(r'Final_model')
tags = mm.processData(nlp,text)
f = open('tags_orihginal.txt','w+')
for i,j in tags.items():
    f.write(i)
    f.write(str(j))
f.close()