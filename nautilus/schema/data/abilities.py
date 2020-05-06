"""Contains object data resolvers."""
from ariadne import ObjectType
from nautilus import utils

abilities_type = ObjectType("Abilities")


@abilities_type.field("main")
def resolve_main(obj, _):
    """Abilities AbilitiesData."""
    return get_ability(obj['main'])


@abilities_type.field("subs")
def resolve_subs(obj, _):
    """Abilities [AbilitiesData]."""
    return [get_ability(i) for i in obj['subs']]


def get_ability(id):
    """Return the ability in abilities.json with the corresponding id."""
    all_abilities = utils.dbh.get_abilities_json()
    try:
        return next(filter(lambda i: i["id"] == id, all_abilities))
    except StopIteration:
        return None
