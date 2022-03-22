from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Welcome"


@app.route("/base")
def base(data="something"):
    return data.upper()
