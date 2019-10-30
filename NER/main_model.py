# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:46:59 2019

@author: tanma
"""

from __future__ import unicode_literals, print_function
import pickle
import plac
import random
from pathlib import Path
import spacy
# spacy.require_gpu()
from spacy.util import minibatch, compounding
import json


def initModel(model = None, new_model_name= 'Final_model' , output_dir= r'Final_model_alt', n_iter=10, filename = r'traindata'):

    # New entity labels
    # Specify the new entity labels which you want to add here
    LABEL = ['COURTNAME', 'PETITIONER', 'DATE' , 'RESPONDENT', 'ACTS', 'JUDGE']

    # Loading training data 
    with open (filename, 'rb') as fp:
        TRAIN_DATA = pickle.load(fp)

    """Setting up the pipeline and entity recognizer, and training the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spacy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe('ner')

    for i in LABEL:
        ner.add_label(i)   # Add new entity labels to entity recognizer

    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.entity.create_optimizer()

    # Get names of other pipes to disable them during training to train only NER
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for i in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            batches = minibatch(TRAIN_DATA, size=compounding(4., 32., 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35,
                           losses=losses)
            print('Losses', losses)


    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

    return nlp



def processData(nlp,text):

    LABEL = ['COURTNAME', 'PETITIONER', 'DATE' , 'RESPONDENT', 'ACTS', 'JUDGE','ALL']

    tags = {}
    for i in LABEL:
        tags[i] = []


    doc = nlp(text)
    print("Entities in '%s'" % text)
    for ent in doc.ents:
        print('-------------------------------------')
        print(ent.label_ + ": " + ent.text)
        tags[ent.label_].append(ent.text)
        tags['ALL'].append(ent.text)


    for key, value in tags.items():
        tags[key] = list(dict.fromkeys(value).keys())
    

    # Adding the results to a new .json document
    # with open('Results.json' ,'w') as f:
    # 	json.dump(tags ,f, indent=2)
    return tags