import json
import requests
import time

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

file = open('course_data.json')
def load_data(file):
    course_data = json.load(file)
    for i in range(len(course_data)):
        print(i)
        name = "course" + str(i + 1)
        print(type(course_data))
        data = course_data[name]
        print(data)
        print(requests.post(url='http://localhost:9200/course/_doc/' + str(i),
                            data=json.dumps(data), headers=headers).json())



def search(entity):
    temp = requests.get(url='http://localhost:9200/course/_search',
                        data='{ "query": { "match" : { "num": { "query": "' + s + '", "fuzziness": "2" } } } }',
                        headers=headers).json()


# ests.post(url='http://localhost:9200/course/'+'0', data=data1, headers=headers).json()
print("----------------------")
# temp = requests.get(url='http://localhost:9200/course/_search?q=num:CSE').json()
s = 'CSE22'

# hits1 = temp['hits']
#
# hits2 = hits1['hits']
# info = hits2[0]['_source']
# info['track']
# print(temp)
# print(requests.delete(url='http://localhost:9200/_all').json())