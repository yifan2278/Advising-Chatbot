from http.server import HTTPServer, BaseHTTPRequestHandler
from wsgiref.handlers import SimpleHandler
import requests
import pickle
import spacy
import numpy as np

# curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http://localhost:8000


with open('./classifier/clf.pkl', 'rb') as f:
    clf = pickle.load(f)
ner_class = spacy.load('./ner/ner_course/')
ner_person = spacy.load('./ner/ner_person/')


def get_class(clf, q):
    prob = clf.predict_proba([q])
    res = 'GREETING'
    if np.max(prob) > 0.19:
        res = clf.classes_[np.argmax(prob)]
    # res = clf.classes_[np.argmax(prob)]
    # print('class:', res, np.max(prob))
    return res


def get_course_entity(ner_class, q):
    try:
        return ner_class(q).ents[0]
    except:
        return None


def get_person_entity(ner_person, q):
    doc = ner_person(q)
    res = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            res.append(ent)
    return res


class fooHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("content-type", 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len).decode("utf-8")
        # print(type(post_body))
        # print(post_body)
        res = self.foo(post_body)
        # print(type(res))
        # print(type(res.encode()))
        self.wfile.write(res.encode())

    def foo(self, data):
        # print(data)
        # r = requests.get(url='http://google.com')
        # return r.text
        q = data
        q_class = get_class(clf, q)
        if q_class == 'GREETING':
            res = "Hi! I'm CSE Advising Chatbot. You can ask me general questions like TODO"
        elif q_class == 'PREREQ':
            class_num = get_course_entity(ner_class, q.lower())
            res = 'The prerequisites for {} is : {}'.format(ner_class, str(class_num))
        elif q_class == 'SIMILAR-COURSES':
            class_num = get_course_entity(ner_class, q.lower())
            res = 'entity:' + str(class_num)
        elif q_class == 'RELATED-COURSES-AI':
            res = q_class
        elif q_class == 'RELATED-COURSES-PYTHON':
            res = q_class
        elif q_class == 'TOPICS':
            class_num = get_course_entity(ner_class, q.lower())
            res = 'entity:' + str(class_num)
        elif q_class == 'WHO-TEACH':
            class_num = get_course_entity(ner_class, q.lower())
            res = 'entity:' + str(class_num)
        elif q_class == 'TEACH-WHAT':
            person = get_person_entity(ner_person, q)
            res = 'entity:' + str(person)
        elif q_class == 'AVAILABLE-SEC':
            class_num = get_course_entity(ner_class, q.lower())
            res = 'entity:' + str(class_num)
        elif q_class == 'GOODBYE':
            res = 'Goodbye!'
        else:
            res = 'Currently not supported'
        print(res)
        return q_class + '\n' + res
        # return data.upper()


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), fooHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
