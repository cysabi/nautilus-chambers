"""Contains all resolvers that return AbilitiesData."""
from ariadne import ObjectType
from nautilus import utils

abilities_type = ObjectType("Abilities")


@abilities_type.field("main")
def resolve_main(obj, _):
    """main: AbilitiesData."""
    return utils.object_data.get_object_by_id('abilities', obj['main'])


@abilities_type.field("subs")
def resolve_subs(obj, _):
    """subs: [AbilitiesData]."""
    return [utils.object_data.get_object_by_id('abilities', i) for i in obj['subs']]
