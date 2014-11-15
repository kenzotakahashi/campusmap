from flask import Flask
from pymongo import MongoClient
import os

# Format: MONGOHQ_URL: mongodb://<user>:<pass>@<base_url>:<port>/<url_path>
if os.environ.get('MONGOHQ_URL'):
    client = MongoClient(os.environ['MONGOHQ_URL'])
    db = client.app31620493
else:
    client = MongoClient()
    db = client.campusmap

app = Flask(__name__)

# client = MongoClient()
# db = client.campusmap

from app import views