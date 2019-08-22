import pymongo


class DBHandler:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["nautilus-chambers"]
        self.col = self.db["profiles"]

    def get_field(self, obj, info):
        parents = self.get_path([], info.path)[1:]
        result = self.col.find_one(
            obj["input"], {
                "_id": 0,
                ".".join(parents): 1
            }
        )
        for key in parents:
            result = result[key]
        return result

    def pass_field(self, obj, info):
        return obj

    def get_path(self, parents, info_path):
        parents.insert(0, info_path.key)
        if info_path.prev:
            self.get_path(parents, info_path.prev)
        return parents
