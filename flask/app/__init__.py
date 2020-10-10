from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://daart:user1243@mongodb:27017/demo'
mongo = PyMongo(app)

CORS(app)
db = mongo.db
app.db = db
print(db)
print(mongo)

from app import views