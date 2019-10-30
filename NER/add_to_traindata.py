# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:00:45 2019

@author: tanma
"""
import json
import pickle 
import re

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

def trim_entity_spans(data: list) -> list:
    """Removes leading and trailing white spaces from entity spans.
    Args:
        data (list): The data to be cleaned in spaCy JSON format.
    Returns:
        list: The cleaned data.
    """
    invalid_span_tokens = re.compile(r'\s')

    cleaned_data = []
    for text, annotations in data:
        entities = annotations['entities']
        valid_entities = []
        for start, end, label in entities:
            valid_start = start
            valid_end = end
            while valid_start < len(text) and invalid_span_tokens.match(
                    text[valid_start]):
                valid_start += 1
            while valid_end > 1 and invalid_span_tokens.match(
                    text[valid_end - 1]):
                valid_end -= 1
            valid_entities.append([valid_start, valid_end, label])
        cleaned_data.append([text, {'entities': valid_entities}])

    return cleaned_data


cleaned_data = trim_entity_spans(add_to_traindata("testData (1).json"))

with open(r'traindata_new', 'wb') as fp:
    pickle.dump(cleaned_data, fp)