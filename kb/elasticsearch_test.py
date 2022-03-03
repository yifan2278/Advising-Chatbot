import json
import requests
import time

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


data1 = {"course1": {
    "num": "CSE5914",
    "prereq": "3521 or 5521, and 2501 or Phil 1338, and CSE 3901 or 3902 or 3903, and 2nd writing; or grad standing.",
    "track": "Artificial intelligence (AI)",
    "topic": "AI, knowledge-base, project",
    "name": "Capstone Design: Knowledge-Based Systems",
    "desc": "Capstone design project; conceptual and technical design; theory and practice of knowledge-based systems; teamwork, written and oral communication skills."
  }}
#
# temp = {
#     "num": "CSE5914",
#     "prereq": "3521 or 5521, and 2501 or Phil 1338, and CSE 3901 or 3902 or 3903, and 2nd writing; or grad standing.",
#     "track": "Artificial intelligence (AI)",
#     "topic": "AI, knowledge-base, project",
#     "name": "Capstone Design: Knowledge-Based Systems",
#     "desc": "Capstone design project; conceptual and technical design; theory and practice of knowledge-based systems; teamwork, written and oral communication skills."
#   }

f = open('course_data.json')
course_data = json.load(f)
#course_data = json.dumps(course_data)
# for i in range(len(course_data)):
#     print(i)
#     name = "course"+str(i+1)
#     print(type(course_data))
#     data = course_data[name]
#     print(data)
#     print(requests.post(url='http://localhost:9200/course/'+str(i),
#                         data=json.dumps(data), headers=headers))
# requests.post(url='http://localhost:9200/course/1', data=temp, headers=headers).json()
# print(requests.get(url='http://localhost:9200/course/1/topic').json())


# requ
# ests.post(url='http://localhost:9200/course/'+'0', data=data1, headers=headers).json()
print("----------------------")
temp = requests.get(url='http://localhost:9200/course/_search?q=num:cse 5911').json()
# hits1 = temp['hits']
# hits2 = hits1['hits']
# hits3 = hits2['hits']
print(hits2)
