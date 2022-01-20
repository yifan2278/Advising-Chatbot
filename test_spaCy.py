import spacy
from spacy.training import Example
import random

nlp = spacy.blank('en')  # new, empty model. Let’s say it’s for the English language
nlp.vocab.vectors.name = 'example_model_training'   # give a name to our list of vectors
nlp.add_pipe('ner', last=True)  # we add the pipeline to the model
ner = nlp.get_pipe("ner")

DATA = [
  (u"What is the prereq for CSE 5914 ", {'entities': [ (23,31,'COURSE') ] }),
  (u"Whats the prereq for CSE 5523 ", {'entities': [ (21,29,'COURSE') ] }),
  (u"Prereq for CSE 3521 ", {'entities': [ (11,19,'COURSE') ] }),
  (u"CSE3521 topics", {'entities': [ (0,7,'COURSE') ] }),
  (u"What is the prereq for cse 5914 ", {'entities': [ (23,31,'COURSE') ] }),
  (u"Whats the prereq for cse 5523 ", {'entities': [ (21,29,'COURSE') ] }),
  (u"Prereq for cse 3521 ", {'entities': [ (11,19,'COURSE') ] }),
  (u"cse3521 topics", {'entities': [ (0,7,'COURSE') ] }),
]

# add labels
for _, annotations in DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

optimizer = nlp.begin_training()
losses = {}
for i in range(100):
    if i % 10 == 0:
        print(i)
    random.shuffle(DATA)
    for batch in spacy.util.minibatch(DATA, size=2):
        for text, annotations in batch:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], sgd=optimizer, losses=losses, drop=0.3)
print(losses)

doc = nlp(u"Available sections of CSE2231")
print(doc.ents)
for entity in doc.ents:
    print(entity.label_, ' | ', entity.text)

# # save model
# nlp.to_disk(output_dir)
# # load the saved model
# nlp = spacy.load(output_dir)