import spacy
from spacy.training import Example
import random

nlp = spacy.load("en_core_web_sm")

s = 'Our team members include Yifan Zhu, Tingyang Xie, Yuan Hong, Leon Cai, and Yiqiao Liao'
doc = nlp(s)

for ent in doc.ents:
    if ent.label_ == 'PERSON':
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


