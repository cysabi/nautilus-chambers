from ariadne import ObjectType
from nautilus import dbh

gear_type = ObjectType("Gear")


@gear_type.field("weapon")
def resolve_weapon(obj, info):
    return "Kensa Tetra Dualies"


@gear_type.field("head")
def resolve_head(obj, info):
    return obj


@gear_type.field("clothes")
def resolve_clothes(obj, info):
    return obj


@gear_type.field("shoes")
def resolve_shoes(obj, info):
    return obj
