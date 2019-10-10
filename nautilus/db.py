import mongomock
from bson.errors import InvalidId
from bson.objectid import ObjectId


class DBHandler:

    def __init__(self):
        self.client = mongomock.MongoClient()
        self.db = self.client.db
        self.col = self.db.collection

    def get_path(self, info_path, parents=None):
        parents = parents if parents else []
        parents.insert(0, info_path.key)
        if info_path.prev:
            self.get_path(info_path.prev, parents)
        if 'profile' in parents:
            parents = parents[parents.index('profile') + 1:]
        return parents

    @classmethod
    def deepmerge(cls, a, b):
        for key, value in b.items():
            a[key] = value if not isinstance(value, dict) \
                else cls.deepmerge(a[key], value)
        return a

    @staticmethod
    def replace_id(dict_to_parse):
        try:
            key = ObjectId(dict_to_parse['discord'])
        except InvalidId:
            key = dict_to_parse['discord']

        dict_to_parse['_id'] = key
        dict_to_parse.pop('discord')
        return dict_to_parse

    empty_profile = {
        "discord": None,
        "meta": {
            "hidden": None
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
    errors = {
        'missing':
        "Profile either doesn't exist, or you do not have permission to see it",
        'empty':
        "Profile is empty, or isn't any different from current profile"
    }
