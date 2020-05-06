"""Contains all resolvers that return WearData."""
from ariadne import ObjectType
from nautilus import utils

wearhead_type = ObjectType("WearHead")
wearclothes_type = ObjectType("WearClothes")
wearshoes_type = ObjectType("WearShoes")


@wearhead_type.field("data")
def resolve_head(obj, _):
    """head: HeadData."""
    return utils.object_data.get_object_by_id('head', obj['id'])


@wearclothes_type.field("data")
def resolve_clothes(obj, _):
    """clothes: ClothesData."""
    return utils.object_data.get_object_by_id('clothes', obj['id'])


@wearshoes_type.field("data")
def resolve_shoes(obj, _):
    """shoes: ShoesData."""
    return utils.object_data.get_object_by_id('shoes', obj['id'])
