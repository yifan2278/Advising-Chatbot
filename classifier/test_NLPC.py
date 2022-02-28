import json
import requests, sys, os


headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

model = os.listdir('classifier/nlpc_data/models/CHATBOT/')[0]
model = model[: model.index('.')]
print(model)

pred_url = "http://localhost:8081/languageclassifier/data/CHATBOT/{}".format(model)
pred_data = '''[
                "prereq of cse 5523",
                "class teaches similar topics to cse3521",
                "show me the classes related to ai",
                "show me the classes related to artificial intelligence",
                "what is cse5914 about",
                "who teaches cse 5914",
                "professor teaching cse5914",
                "what does john doe teach",
                "available sections of cse 5914",
                "go bucks",
                "the quick brown fox jumps over the lazy dog",
                "mocha"
            ]'''
pred_r = requests.post(pred_url, data=pred_data, headers=headers)
print('########### pred ###########')
print(pred_r.json())