import requests
import spacy
import pickle
import numpy as np


def get_class(clf, q):
    prob = clf.predict_proba([q])
    res = 'GREETING'
    if np.max(prob) > 0.2:
        res = clf.classes_[np.argmax(prob)]
    return res


if __name__ == '__main__':
    with open('./classifier/clf.pkl', 'rb') as f:
        clf = pickle.load(f)
    print(get_class(clf, 'what are the ai related classes'))