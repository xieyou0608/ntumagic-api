from flask import Flask
from flask_pymongo import pymongo
from app import app
import os

DATABASES = {
      'default': {
        'CONNECTION_STRING': os.getenv('CONNECTION_STRING'),
        'DB_NAME': os.getenv('DB_NAME'),
    }
}

CONNECTION_STRING = DATABASES['default']['CONNECTION_STRING']
print(CONNECTION_STRING)
myclient = pymongo.MongoClient(CONNECTION_STRING)
mydb = myclient.get_database(DATABASES['default']["DB_NAME"])
user_collection = pymongo.collection.Collection(mydb, 'user_collection')
