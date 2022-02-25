import json
import requests, sys, os


headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

model = os.listdir('classifier/nlpc_data/models/CHATBOT/')[0]
model = model[: model.index('.')]

pred_url = "http://localhost:8081/languageclassifier/data/CHATBOT/{}".format(model)
pred_data = '''[  "Show me the classes related to AI",
                "Who teaches cse 5914",
                "What is cse5914 about",
                "Go Bucks!!!!!!!!!!!!!",
                "The quick brown fox jumps over the lazy dog",
                "mocha"]'''
pred_r = requests.post(pred_url, data=pred_data, headers=headers)
print(pred_r.json())