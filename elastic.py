import json
import requests
import time

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
f = open('course_data.json')
course_data = json.load(f)

for i in range(len(course_data)):
    print(i)
    name = "course"+str(i+1)
    print(type(course_data))
    data = course_data[name]
    print(requests.post(url='http://localhost:9200/course/'+str(i),
                        data=data, headers=headers).json())
print("----------------------")
print(requests.get(url='http://localhost:9200/course/_search?q=2221').json())
