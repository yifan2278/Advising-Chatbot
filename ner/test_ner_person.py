import spacy

# nlp = spacy.load("en_core_web_sm")
# # save model
# nlp.to_disk('./ner/ner_person/')

# load the saved model
nlp = spacy.load('./ner/ner_person/')

s = 'Our team members include Yifan Zhu, Tingyang Xie, Yuan Hong, Leon Cai, and Yiqiao Liao'
doc = nlp(s)

for ent in doc.ents:
    if ent.label_ == 'PERSON':
        print(ent.text, ent.start_char, ent.end_char, ent.label_)


