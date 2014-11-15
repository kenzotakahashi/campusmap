from flask import Flask
from pymongo import MongoClient
import os

# Format: MONGOLAB_URI: mongodb://<user>:<pass>@<base_url>:<port>/<url_path>
if os.environ.get('MONGOLAB_URI'):
    client = MongoClient(os.environ['MONGOLAB_URI'])
    db = client.heroku_app31620493
else:
    client = MongoClient()
    db = client.campusmap

app = Flask(__name__)

# client = MongoClient()
# db = client.campusmap

from app import views