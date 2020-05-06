"""Contains all resolvers that return WearData."""
from ariadne import ObjectType
from nautilus import utils

wear_type = ObjectType("Wear")


@wear_type.field("data")
def resolve_main(obj, _):
    """head: HeadData."""
    return utils.object_data.get(obj['id'], 'head')
