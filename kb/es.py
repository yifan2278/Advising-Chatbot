import requests
import time
import os
import json
from elasticsearch import Elasticsearch
import logging
#set up path

# search in the KB
def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


def create_index(es_object, index_name = 'classes'):
    created = False
    #index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings":{
            'cse':{
                'properties':{
                    "num":{'type':'text'},
                    'prereq':{'type':'text'},
                    'track':{'type':'text'},
                    'topic':{'type':'text'},
                    'name':{'type':'text'},
                    'desc':{'type':'text'},
                    }}}}
    try:
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created

def load_data(es, directory):
    i = 1
    for filename in os.listdir(directory):
       if filename.endswith('course_data.json'):
             f = open(directory+'/'+filename)
             docket_content = f.read()
             es.index(index = 'classes', ignore =400, id = i, body = json.loads(docket_content))
       i = i+1
def search (es_object, index_name, search):
    res = es_object.search(index = index_name, body = search)

if __name__ == '__main__':
    directory = 'C:/Users/123456/Source/Repos/Advising-Chatbot/data/course_data.json'
#connect to es
    logging.basicConfig(level=logging.ERROR)
    es = connect_elasticsearch()
    init_index = create_index(es)
    if not init_index:
        print('Error: fail to create index')
# load json file to elastic search
    load_data(es, directory )
    if es is not None:
        search_object = {
            "query":{
                "match_all":{}
               } }
        res =search(es, 'classes',search_object)
        print(res)
    # delete index
    es.delete(index = 'classes',id = 1,ignore=[400, 404])





