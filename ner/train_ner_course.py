import spacy
from spacy.training import Example
import random


if __name__ == '__main__':
    DATA = [
        (u"What courses do I need to take before cse3521?", {"entities": [ (38, 45, "COURSE") ]}),
        (u"What is cse2431 about?", {"entities": [ (8, 15, "COURSE") ]}),
        (u"Who teaches cse3521?", {"entities": [ (12, 19, "COURSE") ]}),
        (u"What sections of cse2221 are still open?", {"entities": [ (17, 24, "COURSE") ]}),
        (u"What topics does cse2231 cover?", {"entities": [ (17, 24, "COURSE") ]}),
        (u"What content does cse2431 offer?", {"entities": [ (18, 25, "COURSE") ]}),
        (u"What subject will be cse5522 focusing on?", {"entities": [ (21, 28, "COURSE") ]}),
        (u"What topics will be discussed in cse5523?", {"entities": [ (33, 40, "COURSE") ]}),
        (u"What concept will be taught in cse5524?", {"entities": [ (31, 38, "COURSE") ]}),
        (u"What area will cse5525 cover?", {"entities": [ (15, 22, "COURSE") ]}),
        (u"What backgrounds do I need to aquire before taking cse2231?", {"entities": [ (51, 58, "COURSE") ]}),
        (u"What courses are the pre-requisites of cse3345?", {"entities": [ (39, 46, "COURSE") ]}),
        (u"How do I prepare myself before taking cse5525", {"entities": [ (38, 45, "COURSE") ]}),
        (u"What are the courses that covers similar topics compared to cse3521?", {"entities": [ (60, 67, "COURSE") ]}),

        (u"What courses do I need to take before cse 3521?", {"entities": [ (38, 46, "COURSE") ]}),
        (u"What is cse 2431 about?", {"entities": [ (8, 16, "COURSE") ]}),
        (u"Who teaches cse 3521?", {"entities": [ (12, 20, "COURSE") ]}),
        (u"What sections of cse 2221 are still open?", {"entities": [ (17, 25, "COURSE") ]}),
        (u"What topics does cse 2231 cover?", {"entities": [ (17, 25, "COURSE") ]}),
        (u"What content does cse 2431 offer?", {"entities": [ (18, 26, "COURSE") ]}),
        (u"What subject will be cse 5522 focusing on?", {"entities": [ (21, 29, "COURSE") ]}),
        (u"What topics will be discussed in cse 5523?", {"entities": [ (33, 41, "COURSE") ]}),
        (u"What concept will be taught in cse 5524?", {"entities": [ (31, 39, "COURSE") ]}),
        (u"What area will cse 5525 cover?", {"entities": [ (15, 23, "COURSE") ]}),
        (u"What backgrounds do I need to aquire before taking cse 2231?", {"entities": [ (51, 59, "COURSE") ]}),
        (u"What courses are the pre-requisites of cse 3345?", {"entities": [ (39, 47, "COURSE") ]}),
        (u"How do I prepare myself before taking cse 5525", {"entities": [ (38, 46, "COURSE") ]}),
        (u"What are the courses that covers similar topics compared to cse 3521?", {"entities": [ (60, 68, "COURSE") ]}),

        (u"What courses do I need to take before english3521?", {"entities": [(38, 49, "COURSE")]}),
        (u"What is english2431 about?", {"entities": [(8, 19, "COURSE")]}),
        (u"Who teaches english3521?", {"entities": [(12, 23, "COURSE")]}),
        (u"What sections of english2221 are still open?", {"entities": [(17, 28, "COURSE")]}),
        (u"What topics does english2231 cover?", {"entities": [(17, 28, "COURSE")]}),
        (u"What content does english2431 offer?", {"entities": [(18, 29, "COURSE")]}),
        (u"What subject will be english5522 focusing on?", {"entities": [(21, 32, "COURSE")]}),
        (u"What topics will be discussed in english5523?", {"entities": [(33, 44, "COURSE")]}),
        (u"What concept will be taught in english5524?", {"entities": [(31, 42, "COURSE")]}),
        (u"What area will english5525 cover?", {"entities": [(15, 26, "COURSE")]}),
        (u"What backgrounds do I need to aquire before taking english2231?", {"entities": [(51, 62, "COURSE")]}),
        (u"What courses are the pre-requisites of english3345?", {"entities": [(39, 50, "COURSE")]}),
        (u"How do I prepare myself before taking english5525", {"entities": [(38, 49, "COURSE")]}),
        (u"What are the courses that covers similar topics compared to english3521?", {"entities": [(60, 71, "COURSE")]}),
        (u"What courses do I need to take before english 3521?", {"entities": [(38, 50, "COURSE")]}),
        (u"What is english 2431 about?", {"entities": [(8, 20, "COURSE")]}),
        (u"Who teaches english 3521?", {"entities": [(12, 24, "COURSE")]}),
        (u"What sections of english 2221 are still open?", {"entities": [(17, 29, "COURSE")]}),
        (u"What topics does english 2231 cover?", {"entities": [(17, 29, "COURSE")]}),
        (u"What content does english 2431 offer?", {"entities": [(18, 30, "COURSE")]}),
        (u"What subject will be english 5522 focusing on?", {"entities": [(21, 33, "COURSE")]}),
        (u"What topics will be discussed in english 5523?", {"entities": [(33, 45, "COURSE")]}),
        (u"What concept will be taught in english 5524?", {"entities": [(31, 43, "COURSE")]}),
        (u"What area will english 5525 cover?", {"entities": [(15, 27, "COURSE")]}),
        (u"What backgrounds do I need to aquire before taking english 2231?", {"entities": [(51, 63, "COURSE")]}),
        (u"What courses are the pre-requisites of english 3345?", {"entities": [(39, 51, "COURSE")]}),
        (u"How do I prepare myself before taking english 5525", {"entities": [(38, 50, "COURSE")]}),
        (u"What are the courses that covers similar topics compared to english 3521?", {"entities": [(60, 72, "COURSE")]}),

        (u"What courses do I need to take before math3521?",{"entities": [ (38, 46, "COURSE") ]}),
        (u"What is math2431 about?",{"entities": [ (8, 16, "COURSE") ]}),
        (u"Who teaches math3521?",{"entities": [ (12, 20, "COURSE") ]}),
        (u"What sections of math2221 are still open?",{"entities": [ (17, 25, "COURSE") ]}),
        (u"What topics does math2231 cover?",{"entities": [ (17, 25, "COURSE") ]}),
        (u"What content does math2431 offer?",{"entities": [ (18, 26, "COURSE") ]}),
        (u"What subject will be math5522 focusing on?",{"entities": [ (21, 29, "COURSE") ]}),
        (u"What topics will be discussed in math5523?",{"entities": [ (33, 41, "COURSE") ]}),
        (u"What concept will be taught in math5524?",{"entities": [ (31, 39, "COURSE") ]}),
        (u"What area will math5525 cover?",{"entities": [ (15, 23, "COURSE") ]}),
        (u"What backgrounds do I need to aquire before taking math2231?",{"entities": [ (51, 59, "COURSE") ]}),
        (u"What courses are the pre-requisites of math3345?",{"entities": [ (39, 47, "COURSE") ]}),
        (u"How do I prepare myself before taking math5525",{"entities": [ (38, 46, "COURSE") ]}),
        (u"What are the courses that covers similar topics compared to math3521?",{"entities": [ (60, 68, "COURSE") ]}),
        (u"What courses do I need to take before math 3521?",{"entities": [ (38, 47, "COURSE") ]}),
        (u"What is math 2431 about?",{"entities": [ (8, 17, "COURSE") ]}),
        (u"Who teaches math 3521?",{"entities": [ (12, 21, "COURSE") ]}),
        (u"What sections of math 2221 are still open?",{"entities": [ (17, 26, "COURSE") ]}),
        (u"What topics does math 2231 cover?",{"entities": [ (17, 26, "COURSE") ]}),
        (u"What content does math 2431 offer?",{"entities": [ (18, 27, "COURSE") ]}),
        (u"What subject will be math 5522 focusing on?",{"entities": [ (21, 30, "COURSE") ]}),
        (u"What topics will be discussed in math 5523?",{"entities": [ (33, 42, "COURSE") ]}),
        (u"What concept will be taught in math 5524?",{"entities": [ (31, 40, "COURSE") ]}),
        (u"What area will math 5525 cover?",{"entities": [ (15, 24, "COURSE") ]}),
        (u"What backgrounds do I need to aquire before taking math 2231?",{"entities": [ (51, 60, "COURSE") ]}),
        (u"What courses are the pre-requisites of math 3345?",{"entities": [ (39, 48, "COURSE") ]}),
        (u"How do I prepare myself before taking math 5525",{"entities": [ (38, 47, "COURSE") ]}),
        (u"What are the courses that covers similar topics compared to math 3521?",{"entities": [ (60, 69, "COURSE") ]})
    ]

    nlp = spacy.blank('en')  # new, empty model. Let’s say it’s for the English language
    nlp.vocab.vectors.name = 'example_model_training'   # give a name to our list of vectors
    nlp.add_pipe('ner', last=True)  # we add the pipeline to the model
    ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    optimizer = nlp.begin_training()
    losses = {}
    for i in range(3):
        print(i)
        random.shuffle(DATA)
        for batch in spacy.util.minibatch(DATA, size=8):
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], sgd=optimizer, losses=losses, drop=0.2)
        print(losses)

    doc = nlp(u"Available sections of ece 2020")
    print(doc.ents)
    doc = nlp(u"Available sections of cse 3521")
    print(doc.ents)
    doc = nlp(u"Available sections of cse1110")
    print(doc.ents)
    doc = nlp(u"Available sections of ece2020")
    print(doc.ents)
    doc = nlp(u"Available sections of ise 7200")
    print(doc.ents)
    doc = nlp(u"Available sections of math 7200")
    print(doc.ents)
    doc = nlp(u"Available sections of chem 7200")
    print(doc.ents)

    # save model
    # nlp.to_disk('./ner/ner_course/')
    # # load the saved model
    # nlp = spacy.load(output_dir)
