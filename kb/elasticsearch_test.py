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

    print('done')



def search(entity, tag):
    temp = requests.get(url='http://localhost:9200/course/_search',
                        data='{ "query": { "match" : { "num": { "query": "' + entity + '", "fuzziness": "2" } } } }',
                        headers=headers).json()
    hits1 = temp['hits']

    hits2 = hits1['hits']
    info = hits2[0]['_source']
    print(info[tag])

def deleteData():
    print(requests.delete(url='http://localhost:9200/_all').json())



#test

search('CSE2221', 'track')
search('CSE5912', 'name')
search('CSE5914', 'prereq')

