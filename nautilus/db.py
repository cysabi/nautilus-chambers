import pymongo
from json import loads
from bson.objectid import ObjectId
from bson.errors import InvalidId


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
        profile = loads(self.empty_profile)

        self.deepmerge(profile, kwargs['input'])
        query['_id'] = self.col.insert_one(profile).inserted_id

        return {'status': True, 'profile': query}

    def update_profile(self, kwargs):
        query = self.replace_id({'id': kwargs['id']})
        profile = self.col.find_one(query)

        self.deepmerge(profile, kwargs['input'])
        self.col.replace_one(query, profile)

        return {'status': True, 'profile': query}

    def delete_profile(self, kwargs):
        query = self.replace_id({'id': kwargs['id']})

        self.col.delete_one(query)

        return {'status': True}

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
