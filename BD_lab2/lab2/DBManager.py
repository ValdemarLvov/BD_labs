import math
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.code import Code

class DB(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.test

