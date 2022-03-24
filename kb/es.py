
import time
import os
import json
from elasticsearch import Elasticsearch
import logging
# set up path

# search in the KB


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


def create_index(es_object, index_name='classes'):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings": {
            'cse': {
                'properties': {
                    "num": {'type': 'text'},
                    'prereq': {'type': 'text'},
                    'track': {'type': 'text'},
                    'topic': {'type': 'text'},
                    'name': {'type': 'text'},
                    'desc': {'type': 'text'},
                }}}}
    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(
                index=index_name, ignore=400, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def load_data(es, directory):
    f = open(directory)
    course_data = json.load(f)

    for i in range(len(course_data)):
        name = "course" + str(i+1)
        data = course_data[name]
        es.index(index='classes', ignore=400, id=i+1, body=json.dumps(data))


def search(es_object, index_name, search_object):
    search = {
        "query": {
            "multi_match": {
                "query": search_object,
                'fields': []
            }

        }}
    res = es_object.search(index=index_name, body=search)
    return res

    pass


def delete_index(es_object, index_name):
    es_object.indices.delete(index=index_name)




def read_input(filename):
    pass


def delete_index(es_object, index_name):
    es_object.indices.delete(index=index_name)


if __name__ == '__main__':
    directory = 'data/course_data.json'
# connect to es
    logging.basicConfig(level=logging.ERROR)
    es = connect_elasticsearch()
#    init_index = create_index(es)
#    if not init_index:
#        print('Error: fail to create index')
# load json file to elastic search
    # f = open(directory)
    # course_data = json.load(f)
    # for i in range(len(course_data)):
    #     name = "course" + str(i+1)
    #     data = course_data[name]
    #     es.index(index = 'classes',ignore =400, id = i+1, body= json.dumps(data))
    load_data(es, directory)
    if es is not None:

        search_object = "cse5914"
        res = search(es, 'classes', search_object)
        print(res)
    #delete_index(es, "classes")
    #result =search(es, 'classes',search_object)
    # print(result)
    # print(requests.get(url='http://localhost:9200/classes/_search?q=num:cse5914').json())
    # print(requests.delete(url='http://localhost:9200/_all').json())
    # Delete all the local data in es
