from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017/flask_app_db'
mongo = PyMongo(app)

CORS(app)
db = mongo.db.demo2

from app import views