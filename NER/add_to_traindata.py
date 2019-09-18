# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:00:45 2019

@author: tanma
"""
import json

def add_to_traindata(file_name):
    data = json.load(open(file_name,'rb'))
    traindata = []
    what = data['rasa_nlu_data']['common_examples']
    content = what[0]['text']
    annotations = []
    for j in what[0]['entities']:
        if j['entity'] in ['COURTNAME', 'PETITIONER', 'DATE' , 'RESPONDENT', 'ACTS', 'JUDGE']:
            annotations.append((j['start'], j['end'],j['entity']))
            print(content[j['start']:j['end']],'...',j['entity'],'\n')
    
        traindata.append((content, {"entities": annotations}))
    return traindata