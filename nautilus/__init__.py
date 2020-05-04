from ariadne import load_schema_from_path, make_executable_schema
from flask import Flask
from .env import env
from .log import logger

# MongoDB
from .db import dbh

# Araidne
from .schema import bindables
types = load_schema_from_path("nautilus/schema/graphql")
schema = make_executable_schema(types, bindables)

# Flask
app = Flask(__name__)
from . import routes
