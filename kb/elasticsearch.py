import json
import requests
import time

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


def load_data():
    print('ES: Loading data...')
    with open('course_data.json') as file:
        course_data = json.load(file)
    for i in range(len(course_data)):
        # print(i)
        name = "course" + str(i + 1)
        # print(type(course_data))
        data = course_data[name]
        # print(data)
        requests.post(url='http://localhost:9200/course/_doc/' + str(i),
                            data=json.dumps(data), headers=headers).json()
    print('ES: Done!')


def search(entity, tag='', attr='num'):
    entity = entity.upper()
    tag = tag.lower()
    temp = requests.get(url='http://localhost:9200/course/_search',
                        data='{ "query": { "match" : { "' + attr + '": { "query": "' + entity + '", "fuzziness": "2" } } } }',
                        headers=headers).json()
    hits1 = temp['hits']
    hits2 = hits1['hits']
    length = len(hits2)
    # info = hits2[3]['_source']
    listOfResult = []
    # ele = info['hits']
    if not len(entity) == 7:
        for i in range(length):
            result = {}
            info = hits2[i]['_source']
            # print(info['num'])
            if tag == '':
                
                result['num'] = info['num']
                result['name'] = info['name']
                result['track'] = info['track']
                result['prereq'] = info['prereq']
                result['topic'] = info['topic']
                result['desc'] = info['desc']
                result['section'] = info['section']

                print('\n')
                listOfResult.append(result)
            else:
                result[tag] = info[tag]
                listOfResult.append(result)
                # print(tag + ': ' + info[tag])
    else:
        info = hits2[0]['_source']
        result = {}
        if tag == '':

            print('\n')
            result['num'] = info['num']
            result['name'] = info['name']
            result['track'] = info['track']
            result['prereq'] = info['prereq']
            result['topic'] = info['topic']
            result['desc'] = info['desc']
            result['section'] = info['section']
            listOfResult.append(result)
        else:
            # print(tag + ': ' + info[tag])
            result[tag] = info[tag]
            listOfResult.append(result)
    return listOfResult

def deleteData():
    print(requests.delete(url='http://localhost:9200/_all').json())

load_data()
list = search('cse352')
for i in range(len(list)):
    for k,v in list[i].items():
        print(k,v)
    print('\n')
deleteData()