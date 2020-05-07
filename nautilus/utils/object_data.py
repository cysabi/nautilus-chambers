"""Functions that return json documents containing data of all objects of the particular object type."""
import requests


def get_object_by_id(obj: str, id, weapon_id=None):
    """Return the object from the json document with the corresponding id."""
    json_data = requests.get(f'https://gist.githubusercontent.com/LeptoFlare/00bd27c4e27158bdc302ffccc2a91931/raw/{obj}.json').json()
    try:
        data = next(filter(lambda i: i["id"] == id, json_data))
        if weapon_id:
            data = next(filter(lambda i: i["id"] == weapon_id, data["weapons"]))

    except StopIteration:
        return None
    return data
