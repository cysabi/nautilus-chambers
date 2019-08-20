import pymongo


class DBHandler:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["nautilus-chambers"]
        self.collection = self.database["profiles"]
