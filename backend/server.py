from http.server import HTTPServer, BaseHTTPRequestHandler
from wsgiref.handlers import SimpleHandler
import requests
import pickle
import spacy
import numpy as np
import elasticsearch as es
import util

# curl -X POST -H "Content-Type: text/plain" --data "this is raw data" http://localhost:8000


with open('./classifier/clf.pkl', 'rb') as f:
    clf = pickle.load(f)
ner_class = spacy.load('./ner/ner_course/')
ner_person = spacy.load('./ner/ner_person/')


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
        q = data
        q_class = util.get_class(clf, q)

        if q_class == 'GREETING':
            res = """Hi! I'm CSE Advising Chatbot. You can ask me general questions 
                    regarding prereqs, AI classes, available sections, etc."""

        elif q_class == 'PREREQ':
            class_num = util.get_course_entity(ner_class, q.lower())
            prereqs = es.search(class_num, 'prereq')
            res = 'The prerequisites for {} is : {}'.format(class_num, prereqs)

        elif q_class == 'SIMILAR-COURSES':
            class_num = util.get_course_entity(ner_class, q.lower())
            track = es.search(class_num, tag='track')
            sim_course = es.search(track[0]['track'], tag='num', attr='track')
            res = 'Courses similar to {} are: {}'.format(class_num, sim_course)

        elif q_class == 'RELATED-COURSES-AI':
            ai_course = es.search('artificial intelligence', tag='num', attr='track')
            res = 'The AI related courses are {}'.format(ai_course)

        elif q_class == 'RELATED-COURSES-PYTHON':
            py_course = es.search('python', tag='num', attr='topic')
            res = 'The Python related courses are {}'.format(py_course)

        elif q_class == 'TOPICS':
            class_num = util.get_course_entity(ner_class, q.lower())
            desc = es.search(class_num, tag='topic')
            res = '{}: {}'.format(class_num, desc)

        elif q_class == 'WHO-TEACH':
            class_num = util.get_course_entity(ner_class, q.lower())
            prof = es.search(class_num, tag='section')
            res = 'The instructor for {} is/are {}'.format(class_num, prof)

        elif q_class == 'TEACH-WHAT':
            person = util.get_person_entity(ner_person, q)
            course = es.search(person, tag='num', attr='section')
            res = 'entity:' + person + str(course)

        elif q_class == 'AVAILABLE-SEC':
            class_num = util.get_course_entity(ner_class, q.lower())
            section = es.search(class_num, tag='section')
            res = 'entity:' + str(class_num) + str(section)

        elif q_class == 'GOODBYE':
            res = 'Goodbye!'

        else:
            res = 'Currently not supported'

        print(res)
        return q_class + '\n' + res


def main():
    es.deleteData()
    es.load_data()

    PORT = 8000
    server = HTTPServer(('', PORT), fooHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

    es.deleteData()


if __name__ == '__main__':
    main()
