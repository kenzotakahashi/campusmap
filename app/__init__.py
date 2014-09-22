from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient()
db = client.campusmap

from app import views