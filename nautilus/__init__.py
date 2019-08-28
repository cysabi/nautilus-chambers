from ariadne import load_schema_from_path, make_executable_schema
from flask import Flask

# PyMongo
from .db import DBHandler
dbh = DBHandler()

# Araidne
from .schema import bindables
types = load_schema_from_path("nautilus/schema/graphql")
schema = make_executable_schema(types, bindables)

# Flask
app = Flask(__name__)
from . import routes
