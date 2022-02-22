import requests
import time

# add data
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
r = requests.get(url='http://localhost:9200')
print(r.json())
print()
data = '{ "num": "CSE5914", "prereq": "CSE 3901, CSE 2501, CSE 3521", "track": "Artificial intelligence (AI)" }'
print(requests.post(url='http://localhost:9200/course/1',
      data=data, headers=headers).json())
# search
time.sleep(2)
s = 'cse 5914'.replace(" ", "")
print(requests.get(url='http://localhost:9200/_search?q=cse').json())
print(requests.get(url='http://localhost:9200/_search',
      data='{ "query": { "match" : { "num": { "query": "' + s + '", "fuzziness": "AUTO" } } } }', headers=headers).json())
print(requests.get(url='http://localhost:9200/_search',
      data='{ "query": { "match" : { "track": { "query": "ai", "fuzziness": "AUTO" } } } }', headers=headers).json())
# delete all
print(requests.delete(url='http://localhost:9200/_all').json())
