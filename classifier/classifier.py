import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import SVC
import json, sys


with open('./data/user_data_preprocessed.json', 'r') as f:
    user_data_str = f.read()
data = json.loads(user_data_str)

X = []
y = []
for d in data:
    X.append(d['passage'])
    y.append(d['label'])


text_clf = Pipeline([
        ('vect', CountVectorizer(ngram_range=(1,2))),
        ('clf', LogisticRegression()),
    ])

pred_data = [
                "hi",
                'good morning',
                'whats up',
                "bye",
                "see you",
                "thank you",
                "prereq for cse 5523",
                'what are the prereqs for cse 5523',
                "class teaches similar topics to cse3521",
                "simlar classes to ece3521",
                "show me the courses related to ai",
                "show me the courses teaching ai",
                "show me the courses about ai",
                "show me the classes related to artificial intelligence",
                "what is cse5914 about",
                "who teaches cse 5914",
                "professor teaching cse5914",
                "what does john doe teach",
                "available sections of cse 5914",
                "go bucks",
                "the quick brown fox jumps over the lazy dog",
                "mocha"
            ]

text_clf.fit(X, y)
print(text_clf.predict(pred_data))
print(np.max(text_clf.predict_proba(pred_data), axis=1))

y_pred = []
for p in text_clf.predict_proba(pred_data):
    if np.max(p) < 0.2:
        y_pred.append('GREETING')
    else:
        y_pred.append(text_clf.classes_[np.argmax(p)])
print(y_pred)

import pickle

# with open('./classifer/clf.pkl', 'wb') as f:
#     pickle.dump(text_clf, f)

# and later you can load it
# with open('./classifier/clf.pkl', 'rb') as f:
#     text_clf = pickle.load(f)
