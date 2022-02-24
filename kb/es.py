import requests
import time
import os
import json
from elasticsearch import Elasticsearch
#set up path
directory = 'C:/Users/123456/Source/Repos/Advising-Chatbot/data'
res = requests.get('http://localhost:9200')
print(res.content)
es = Elasticsearch('http://localhost:9200')
es.info()
i = 1
# load json file to elastic search
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        print(filename)
        f = open(directory+'/'+filename)
        docket_content = f.read()
        es.index(index = 'myindex', ignore =400, id = i, body = json.loads(docket_content))
        i = i+1

# search in the KB




