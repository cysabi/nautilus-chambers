"""Functions that return json documents containing data of all objects of the particular object type."""
import json


def get_object_by_id(obj: str, id, weapon_id=None):
    """Return the object from the json document with the corresponding id."""
    with open(f'docs/dumps/loadout-ink/{obj}.json') as f:
        json_data = json.load(f)
    try:
        data = next(filter(lambda i: i["id"] == id, json_data))
        if weapon_id is not None:
            data = next(filter(lambda i: i["id"] == weapon_id, data["weapons"]))

    except StopIteration:
        return None
    return data


def get_rank(name: str = None, value: int = None):
    """Return the rank name or power from the json document with the corresponding id."""
    with open(f'docs/dumps/rank-powers/jp.json') as f:
        json_data = json.load(f)
    for n, v in json_data:
        if n == name:
            return v
        if v == value:
            return n
