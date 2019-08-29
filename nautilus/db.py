import pymongo


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

    @staticmethod
    def replace_id(dict_to_parse):
        dict_to_parse['_id'] = dict_to_parse.pop('id')
        return dict_to_parse

    @staticmethod
    def update_profile(a: dict, b: dict) -> None:

        def _process(_a: dict, _b: dict) -> None:

            for key, value in _b.items():
                if not isinstance(value, dict):
                    _a[key] = value
                else:
                    if key not in _a:
                        _a[key] = {}
                    _process(_a[key], value)

        _process(a, b)
        return a
