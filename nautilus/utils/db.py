"""Set up database client."""
from . import env

if env.get("debug"):
    from mongomock import MongoClient
else:
    from pymongo import MongoClient


class DatabaseHandler:
    """Custom database handler that works with mongodb."""

    def __init__(self):
        # Client & Database
        self.client = MongoClient("mongodb://mongo:27017/")
        self.db = self.client["nautilus"]
        # Collections
        self.profiles = self.db["profiles"]
        self.abilitysets = self.db["abilities"]

    @staticmethod
    def empty_profile():
        """Create a new empty profile."""
        return {
            "meta": {
                "private": None
            },
            "status": {
                "ign": None,
                "sw": None,
                "level": None,
                "rank": {
                    "sz": None,
                    "tc": None,
                    "rm": None,
                    "cb": None,
                    "sr": None,
                },
                "gear": {
                    "weapon": None,
                    "head":    {"id": None, "abilities": None},
                    "clothes": {"id": None, "abilities": None},
                    "shoes":   {"id": None, "abilities": None}
                }
            }
        }


dbh = DatabaseHandler()
