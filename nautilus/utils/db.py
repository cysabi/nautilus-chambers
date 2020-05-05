"""Set up database client."""
from . import env

if env.get("debug"):
    from mongomock import MongoClient
else:
    from pymongo import MongoClient


class DatabaseHandler:
    """Custom database handler that works with mongodb."""

    def __init__(self):
        self.client = MongoClient("mongodb://mongo:27017/")
        self.db = self.client["nautilus"]
        self.profiles = self.db["profiles"]

    empty_profile = {
        "discord": None,
        "meta": {
            "private": None
        },
        "status": {
            "gear": {
                "clothes": {
                    "abilities": {
                        "main": None,
                        "subs": [None, None, None]
                    },
                    "name": None
                },
                "head": {
                    "abilities": {
                        "main": None,
                        "subs": [None, None, None]
                    },
                    "name": None
                },
                "shoes": {
                    "abilities": {
                        "main": None,
                        "subs": [None, None, None]
                    },
                    "name": None
                },
                "weapon": None
            },
            "ign": None,
            "level": None,
            "rank": {
                "cb": None,
                "rm": None,
                "sr": None,
                "sz": None,
                "tc": None
            }
        }
    }


dbh = DatabaseHandler()
