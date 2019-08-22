from ariadne import ObjectType
from nautilus import dbh

gear_type = ObjectType("Gear")


@gear_type.field("weapon")
def resolve_weapon(obj, info):
    return dbh.get_field(obj, info)


@gear_type.field("head")
def resolve_head(obj, info):
    return dbh.pass_field(obj, info)


@gear_type.field("clothes")
def resolve_clothes(obj, info):
    return dbh.pass_field(obj, info)


@gear_type.field("shoes")
def resolve_shoes(obj, info):
    return dbh.pass_field(obj, info)
