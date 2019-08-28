import pymongo


class DBHandler:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nautilus-chambers"]
        self.col = self.db["profiles"]

    def get_field(self, obj, info):
        parents = self.get_path(info.path)[1:]
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
        return parents
