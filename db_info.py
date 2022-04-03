from flask import Flask
from flask_pymongo import pymongo
from app import app
from setting import DATABASES

CONNECTION_STRING = DATABASES['default']['CONNECTION_STRING']
myclient = pymongo.MongoClient(CONNECTION_STRING)
mydb = myclient.get_database(DATABASES['default']["NAME"])
user_collection = pymongo.collection.Collection(mydb, 'user_collection')
