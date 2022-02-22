import requests
import time
import os
from elasticsearch import Elasticsearch
#set up path
directory = './Advising-Chatbot'
res = requests.get('http://localhost:9200')
print(res.content)
es = Elasticsearch([{'host':'localhost', 'port':'9200'}])
i = 1
# load json file to elastic search
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        f = open(filename)
        docket_content = f.read()
        es.index(index = 'myindex', ignore =400, doc_type = 'docket', id = i, body = json.loads(docket_content))
        i = i+1

# search in the KB




