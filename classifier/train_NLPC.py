import json
import requests, sys


# with open('user_data.json', 'r') as f:
#     user_data_str = f.read()
# data = json.loads(user_data_str)
# with open('user_data_preprocessed.json', 'w+') as f:
#     f.write('[\n')
#     i = 0
#     for sample in data:
#         i += 1
#         x = data[sample]['input']
#         y = data[sample]['label']
#         if i == len(data):
#             f.write('\t{{ "label": "{}", "passage": "{}" }}\n'.format(y, x))
#         else:
#             f.write('\t{{ "label": "{}", "passage": "{}" }},\n'.format(y, x))
#         print(i, end=', ')
#     f.write(']')
# sys.exit()

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# with open('user_data_preprocessed.json', 'r') as f:
#     train_data = f.read()

# # print(train_data)
# train_url = "http://localhost:8081/languageclassifier/data/CHATBOT"
# train_r = requests.post(train_url, data=train_data, headers=headers)
# print(train_r)
# print(train_r.json())

model_url = "http://localhost:8081/model/CHATBOT"
model_data = "{  \"model_name\": \"thisisamodelname\"}"
r = requests.post(model_url, data=model_data, headers=headers)
print(r.json())

pred_url = "http://localhost:8081/languageclassifier/data/CHATBOT/{}".format(r.json())
pred_data = '''[  "Show me the classes related to AI",
                "Who teaches cse 5914",
                "What is cse5914 about",
                "Go Bucks!!!!!!!!!!!!!",
                "The quick brown fox jumps over the lazy dog",
                "mocha"]'''
pred_r = requests.post(pred_url, data=pred_data, headers=headers)
print(pred_r.json())