import requests
import spacy
import pickle
import numpy as np


def get_class(clf, q):
    prob = clf.predict_proba([q])
    # res = 'GREETING'
    # if np.max(prob) > 0.2:
    #     res = clf.classes_[np.argmax(prob)]
    res = clf.classes_[np.argmax(prob)]
    print('class:', res, np.max(prob))
    return res


def get_course_entity(ner_class, q):
    return ner_class(q).ents[0]


def get_person_entity(ner_person, q):
    doc = ner_person(q)
    res = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            res.append(ent)
    return res


def main():
    with open('./classifier/clf.pkl', 'rb') as f:
        clf = pickle.load(f)
    ner_class = spacy.load('./ner/ner_course/')
    ner_person = spacy.load('./ner/ner_person/')

    q = input('Hello!\n')
    q_class = get_class(clf, q)
    while True:#q_class != 'GOODBYE':
        if q_class == 'GREETING':
            print('Hi')
        elif q_class == 'PREREQ':
            class_num = get_course_entity(ner_class, q.lower())
            print('entity:', class_num)
        elif q_class == 'SIMILAR-COURSES':
            class_num = get_course_entity(ner_class, q.lower())
            print('entity:', class_num)
        elif q_class == 'RELATED-COURSES-AI':
            pass
        elif q_class == 'RELATED-COURSES-PYTHON':
            pass
        elif q_class == 'TOPICS':
            class_num = get_course_entity(ner_class, q.lower())
            print('entity:', class_num)
        elif q_class == 'WHO-TEACH':
            class_num = get_course_entity(ner_class, q.lower())
            print('entity:', class_num)
        elif q_class == 'TEACH-WHAT':
            person = get_person_entity(ner_person, q)
            print('entity:', person)
        elif q_class == 'AVAILABLE-SEC':
            class_num = get_course_entity(ner_class, q.lower())
            print('entity:', class_num)
        else:
            print('Currently not supported')
        print()
        q = input('Hello again!\n')
        q_class = get_class(clf, q)

    print('Goodbye!')


if __name__ == '__main__':
    main()