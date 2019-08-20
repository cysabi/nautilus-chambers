import pymongo
from ariadne import load_schema_from_path, make_executable_schema
from flask import Flask


# PyMongo
class DBHandler:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["nautilus-chambers"]
        self.collection = self.database["profiles"]


dbh = DBHandler()

# Araidne
from .schema import bindables
types = load_schema_from_path("nautilus/schema/.graphql")
schema = make_executable_schema(types, bindables)

# Flask
app = Flask(__name__)
from nautilus import routes
