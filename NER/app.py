# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 21:46:53 2019

@author: tanma
"""

import main_model as mm
import pdf_to_text as convert
import load as l
import json
nlp = l.init()


def jsonify(pdf_file_path,nlp = nlp):
    """
    Build an indented .json doc from a legal .pdf document using PDFBox API
    and a spacy NER model using pre-existing labels
    
    # Arguments
        pdf_file_path(string):File path to the PDF you want to convert to entities
        
    # Returns
        results.json:A beautified .json documents containing all the entities
        found in the document
    
    """
    text = convert.convert_pdf_to_text_pdfbox_api(pdf_file_path)
    text = text[:1000000]
    
    tags = mm.processData(nlp,text)
    with open('result.json','w+') as f:
        json.dump(tags,f,indent = 4)