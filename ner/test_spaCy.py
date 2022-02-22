import spacy
from spacy.training import Example
import random


if __name__ == '__main__':
    DATA = [
        (u"What courses do I need to take before CSE3521?", {"entities": [ (38, 45, "COURSE") ]}),
        (u"What is CSE2431 about?", {"entities": [ (8, 15, "COURSE") ]}),
        (u"Who teaches CSE3521?", {"entities": [ (12, 19, "COURSE") ]}),
        (u"What sections of CSE2221 are still open?", {"entities": [ (17, 24, "COURSE") ]}),
        (u"What topics does CSE2231 cover?", {"entities": [ (17, 24, "COURSE") ]}),
        (u"What content does CSE2431 offer?", {"entities": [ (18, 25, "COURSE") ]}),
        (u"What subject will be CSE5522 focusing on?", {"entities": [ (21, 28, "COURSE") ]}),
        (u"What topics will be discussed in CSE5523?", {"entities": [ (33, 40, "COURSE") ]}),
        (u"What concept will be taught in CSE5524?", {"entities": [ (31, 38, "COURSE") ]}),
        (u"What area will CSE5525 cover?", {"entities": [ (15, 22, "COURSE") ]}),
        (u"What backgrounds do I need to aquire before taking CSE2231?", {"entities": [ (51, 58, "COURSE") ]}),
        (u"What courses are the pre-requisites of CSE3345?", {"entities": [ (39, 46, "COURSE") ]}),
        (u"How do I prepare myself before taking CSE5525", {"entities": [ (38, 45, "COURSE") ]}),
        (u"What are the courses that covers similar topics compared to CSE3521?", {"entities": [ (60, 67, "COURSE") ]}),

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

        (u"What courses do I need to take before CSE 3521?", {"entities": [ (38, 46, "COURSE") ]}),
        (u"What is CSE 2431 about?", {"entities": [ (8, 16, "COURSE") ]}),
        (u"Who teaches CSE 3521?", {"entities": [ (12, 20, "COURSE") ]}),
        (u"What sections of CSE 2221 are still open?", {"entities": [ (17, 25, "COURSE") ]}),
        (u"What topics does CSE 2231 cover?", {"entities": [ (17, 25, "COURSE") ]}),
        (u"What content does CSE 2431 offer?", {"entities": [ (18, 26, "COURSE") ]}),
        (u"What subject will be CSE 5522 focusing on?", {"entities": [ (21, 29, "COURSE") ]}),
        (u"What topics will be discussed in CSE 5523?", {"entities": [ (33, 41, "COURSE") ]}),
        (u"What concept will be taught in CSE 5524?", {"entities": [ (31, 39, "COURSE") ]}),
        (u"What area will CSE 5525 cover?", {"entities": [ (15, 23, "COURSE") ]}),
        (u"What backgrounds do I need to aquire before taking CSE 2231?", {"entities": [ (51, 59, "COURSE") ]}),
        (u"What courses are the pre-requisites of CSE 3345?", {"entities": [ (39, 47, "COURSE") ]}),
        (u"How do I prepare myself before taking CSE 5525", {"entities": [ (38, 46, "COURSE") ]}),
        (u"What are the courses that covers similar topics compared to CSE 3521?", {"entities": [ (60, 68, "COURSE") ]}),
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
    for i in range(10):
        print(i)
        # if i % 10 == 0:
        #     print(i)
        random.shuffle(DATA)
        for batch in spacy.util.minibatch(DATA, size=4):
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], sgd=optimizer, losses=losses, drop=0.3)
    print(losses)

    doc = nlp(u"Available sections of ECE 2020")
    print(doc.ents)
    doc = nlp(u"Available sections of ECE2020")
    print(doc.ents)
    doc = nlp(u"Available sections of ece2020")
    print(doc.ents)
    doc = nlp(u"Available sections of ece 2020")
    print(doc.ents)

    # # save model
    # nlp.to_disk('./ner_course/')
    # # load the saved model
    # nlp = spacy.load(output_dir)
