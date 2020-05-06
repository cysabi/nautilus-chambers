"""Contains all resolvers that return AbilitiesData."""
from ariadne import ObjectType
from nautilus import utils

abilities_type = ObjectType("Abilities")


@abilities_type.field("main")
def resolve_main(obj, _):
    """main: AbilitiesData."""
    return utils.object_data.get(obj['main'], 'abilities')


@abilities_type.field("subs")
def resolve_subs(obj, _):
    """subs: [AbilitiesData]."""
    return [utils.object_data.get(i, 'abilities') for i in obj['subs']]
