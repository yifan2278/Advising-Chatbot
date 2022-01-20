import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

train_data = "[  {    \"label\": \"FIRE_PHASERS\",    \"passage\": \"fire a phaser burst, half power\"  },{    \"label\": \"FIRE_PHASERS\",    \"passage\": \"mister worf, fire phasers\"  },{    \"label\": \"FIRE_TORPEDO\",    \"passage\": \"torpedo burst, five second delay\"  },{    \"label\": \"FIRE_TORPEDO\",    \"passage\": \"torpedoes full spread please\"  },{    \"label\": \"FIRE_TORPEDO\",    \"passage\": \"one torpedo should do it\"  },{    \"label\": \"GO_TO_WARP\",    \"passage\": \"increase speed to warp 1\"  },{    \"label\": \"GO_TO_WARP\",    \"passage\": \"let's go to warp\"  },{    \"label\": \"GO_TO_WARP\",    \"passage\": \"helm get us out of here now\"  }]"
train_url = "http://localhost:8081/languageclassifier/data/STAR_TREK"
train_r = requests.post(train_url, data=train_data, headers=headers)
print(train_r)
print(train_r.json())

model_url = "http://localhost:8081/model/STAR_TREK"
model_data = "{  \"model_name\": \"thisisamodelname\"}"
r = requests.post(model_url, data=model_data, headers=headers)
print(r.json())

pred_url = "http://localhost:8081/languageclassifier/data/STAR_TREK/{}".format(r.json())
pred_data = "[  \"ahead warp factor 1, engage\",  \"give me a full torpedo spread one thousand kilometers off the forward bow\"]"
pred_r = requests.post(pred_url, data=pred_data, headers=headers)
print(pred_r.json())
