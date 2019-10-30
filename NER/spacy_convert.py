# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:41:39 2019

@author: tanma
"""

import json
import pickle
from pprint import pprint
import codecs
import re

data = json.load(open(r'final_data.json', encoding='utf-8-sig'))

traindata = []
for i in data['annotations_and_examples']:
    content = i['content']
    annotations = []
    for j in i['annotations']:
        if j['tag'] in ['COURTNAME', 'PETITIONER', 'DATE' , 'RESPONDENT', 'ACTS', 'JUDGE']:
            annotations.append((j['start'], j['end'],j['tag']))
            print(content[j['start']:j['end']],'...',j['tag'],'\n')

    traindata.append((content, {"entities": annotations}))



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


cleaned_data = trim_entity_spans(traindata)

with open(r'traindata', 'wb') as fp:
    pickle.dump(cleaned_data, fp)