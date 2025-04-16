from flask import flask
from pymongo import MongoClient

app = flask(__name__)

client = MongoClient("mongodb+srv://yobinvergara:1006037426yobin@cluster0.hgxyeef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['eter']
collection = db['usuarios']