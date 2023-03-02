import pandas as pd 
import numpy as np
import os 
from os import path

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

#-------basic_clean--------------------------------------------------

def basic_clean(sentence):
    
    '''
    Input: string
    Output: string that is all lower case, normalized, and removed of 
    special characters.
    '''
    
    # lower case
    low_sent = sentence.lower()
    
    # normalize sentence
    norm_sent = unicodedata.normalize('NFKD',low_sent)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    
    # not a-z, #, single quote, or white space
    sentence = re.sub(r"[^a-z0-9'\s]",'', low_sent)
    
    #return sentence
    return sentence

#-------tokenize--------------------------------------------------
def tokenize(sentence):
    
    # create object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    tok_sen = tokenizer.tokenize(sentence, return_str=True)
    
    # lower case
    tok_sen = tok_sen.lower()
    
    return tok_sen


#-------stem--------------------------------------------------

def stem(sentence):
    
    # create the nltk stemmer object
    ps = nltk.porter.PorterStemmer()
    
    # loop, for every word in the sentence perform ps.stem
    stems = [ps.stem(word) for word in sentence.split()]
    
    # join works to string
    sentence_stemmed = ' '.join(stems)
    
    # return string
    return sentence_stemmed
    
    
#-------lemmatize--------------------------------------------------

def lemmatize(sentence):
    
    # create object
    wnl = nltk.stem.WordNetLemmatizer()
    
    # loop, for every word in the sentence perform ps.stem
    lemmas = [wnl.lemmatize(word) for word in sentence.split()]
    
    # join works to string
    sentence_lemmed = ' '.join(lemmas)
    
    return sentence_lemmed
    