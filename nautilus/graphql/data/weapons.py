"""Contains all resolvers that return WeaponData."""
from ariadne import ObjectType
from nautilus import utils

gear_type = ObjectType("Gear")
weapon_type = ObjectType("WeaponData")


@gear_type.field("weapon")
def resolve_weapon(obj, _):
    """weapon: WeaponData."""
    if obj['weapon']:
        return utils.object_data.get_object_by_id('weapons', obj['weapon']['class'], obj['weapon']['id'])


@weapon_type.field("class")
def resolve_weapon_class(obj, _):
    """class: WeaponClassData."""
    if obj['weapon']:
        return utils.object_data.get_object_by_id('weapons', obj['class'])
