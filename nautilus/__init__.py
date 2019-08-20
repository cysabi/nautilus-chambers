from ariadne import ObjectType, make_executable_schema, load_schema_from_path
from flask import Flask
import pymongo

# Araidne
types = load_schema_from_path("nautilus/schema.gql")

query = ObjectType("Query")
greeting = ObjectType("Greeting")

from nautilus import resolvers

schema = make_executable_schema(types, [query, greeting])

# Flask
app = Flask(__name__)
from nautilus import routes


# PyMongo
class DBHandler:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client["nautilus-chambers"]
        self.collection = self.database["profiles"]


dbh = DBHandler()
