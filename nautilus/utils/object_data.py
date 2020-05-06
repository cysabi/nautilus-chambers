"""Functions that return json documents containing data of all objects of the particular object type."""
import requests


def get(id, obj: str):
    """Return the object from the json document with the corresponding id."""
    json_data = requests.get(f'https://gist.githubusercontent.com/LeptoFlare/00bd27c4e27158bdc302ffccc2a91931/raw/{obj}.json').json()
    try:
        return next(filter(lambda i: i["id"] == id, json_data))
    except StopIteration:
        return None
