from json import loads

import pymongo
from bson.errors import InvalidId
from bson.objectid import ObjectId


class DBHandler:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nautilus-chambers"]
        self.col = self.db["profiles"]

    def get_field(self, obj, info):
        parents = self.get_path(info.path)
        result = self.col.find_one(obj, {"_id": 0, ".".join(parents): 1})
        for key in parents:
            result = result[key]
        return result

    def pass_field(self, obj, info):
        return obj

    def get_path(self, info_path, parents=None):
        parents = parents if parents else []
        key = '_id' if info_path.key == 'id' else info_path.key
        parents.insert(0, key)
        if info_path.prev:
            self.get_path(info_path.prev, parents)
        if 'profile' in parents:
            parents = parents[parents.index('profile') + 1:]
        return parents

    def create_profile(self, kwargs):
        query = {'_id': None}
        payload = {}
        profile = loads(self.empty_profile)
        new_profile = kwargs['input']

        # Check for errors
        if new_profile == profile or new_profile == {}:
            payload['error'] = self.errors['empty']

        # All Good
        else:
            self.deepmerge(profile, new_profile)
            query['_id'] = self.col.insert_one(profile).inserted_id
            payload['profile'] = query

        payload['status'] = True if not payload.get('error') else False
        return payload

    def update_profile(self, kwargs):
        query = self.replace_id({'id': kwargs['id']})
        payload = {}
        profile = self.col.find_one(query)
        new_profile = kwargs['input']

        # Check for errors
        if new_profile == profile or new_profile == {}:
            payload['error'] = self.errors['empty']
        elif profile is None:
            payload['error'] = self.errors['missing']

        # All Good
        else:
            self.deepmerge(profile, new_profile)
            self.col.replace_one(query, profile)
            payload['profile'] = query

        payload['status'] = True if not payload.get('error') else False
        return payload

    def delete_profile(self, kwargs):
        query = self.replace_id({'id': kwargs['id']})
        payload = {}
        profile = self.doc_exists(query)

        # Check for errors
        if profile is None:
            payload['error'] = self.errors['missing']

        # All Good
        else:
            self.col.delete_one(query)

        payload['status'] = True if not payload.get('error') else False
        return payload

    def doc_exists(self, query):
        return self.col.find_one(query, {"_id": 1})

    @classmethod
    def deepmerge(cls, a, b):
        for key, value in b.items():
            a[key] = value if not isinstance(value, dict) \
                else cls.deepmerge(a[key], value)
        return a

    @staticmethod
    def replace_id(dict_to_parse):
        try:
            key = ObjectId(dict_to_parse['id'])
        except InvalidId:
            key = dict_to_parse['id']

        dict_to_parse['_id'] = key
        dict_to_parse.pop('id')
        return dict_to_parse

    empty_profile = """{"meta":{"discord":null,"twitter":null},"status":{"gear":{"clothes":{"abilities":{"main":null,"subs":[null,null,null]},"name":null},"head":{"abilities":{"main":null,"subs":[null,null,null]},"name":null},"shoes":{"abilities":{"main":null,"subs":[null,null,null]},"name":null},"weapon":null},"ign":null,"level":null,"rank":{"cb":null,"rm":null,"sr":null,"sz":null,"tc":null}}}"""
    errors = {
        'missing':
        "Profile either doesn't exist, or you do not have permission to see it",
        'empty':
        "Profile is empty, or isn't any different from current profile"
    }
