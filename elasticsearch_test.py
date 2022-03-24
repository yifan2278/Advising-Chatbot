import json
import requests
import time

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


def load_data():
    file = open('course_data.json')
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


def search(entity, tag=''):
    entity = entity.upper()
    tag = tag.lower()
    temp = requests.get(url='http://localhost:9200/course/_search',
                        data='{ "query": { "match" : { "num": { "query": "' + entity + '", "fuzziness": "2" } } } }',
                        headers=headers).json()
    hits1 = temp['hits']
    hits2 = hits1['hits']
    length = len(hits2)
    # info = hits2[3]['_source']

    # ele = info['hits']
    if not len(entity) == 7:
        for i in range(length):
            info = hits2[i]['_source']
            # print(info['num'])
            if tag == '':
                print('num: ' + info['num'])
                print('name: ' + info['name'])
                print('track: ' + info['track'])
                print('prereq: ' + info['prereq'])
                print('topic: ' + info['topic'])
                print('desc:' + info['desc'])
                print('\n')
            else:
                print(tag + ': ' + info[tag])
    else:
        info = hits2[0]['_source']
        if tag == '':
            print('num: ' + info['num'])
            print('name: ' + info['name'])
            print('track: ' + info['track'])
            print('prereq: ' + info['prereq'])
            print('topic: ' + info['topic'])
            print('desc:' + info['desc'])
            print('\n')
        else:
            print(tag + ': ' + info[tag])


def deleteData():
    print(requests.delete(url='http://localhost:9200/_all').json())


search('cse2221', 'prereq')
