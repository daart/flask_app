from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://daart:pass1234@db:27017/flaskdb'
mongo = PyMongo(app)

CORS(app)
db = mongo.db
app.db = db
print(db)
print(mongo)

from app import views
