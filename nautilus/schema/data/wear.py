"""Contains all resolvers that return WearData."""
from ariadne import ObjectType
from nautilus import utils

wearhead_type = ObjectType("WearHead")
wearclothes_type = ObjectType("WearClothes")
wearshoes_type = ObjectType("WearShoes")


@wearhead_type.field("data")
def resolve_head(obj, _):
    """head: HeadData."""
    return utils.object_data.get(obj['id'], 'head')


@wearclothes_type.field("data")
def resolve_clothes(obj, _):
    """clothes: ClothesData."""
    return utils.object_data.get(obj['id'], 'clothes')


@wearshoes_type.field("data")
def resolve_shoes(obj, _):
    """shoes: ShoesData."""
    return utils.object_data.get(obj['id'], 'shoes')
