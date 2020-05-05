"""Set up app and schema."""
from ariadne import load_schema_from_path, make_executable_schema
from flask import Flask
from nautilus import utils

# Araidne
from .schema import bindables
types = load_schema_from_path("nautilus/schema/graphql")
schema = make_executable_schema(types, *bindables)

# Flask
app = Flask(__name__)
from . import routes
