from ariadne import ObjectType
from nautilus import dbh

wear_type = ObjectType("Wear")


@wear_type.field("name")
def resolve_name(obj, info):
    return "TestWear"


@wear_type.field("abilities")
def resolve_abilities(obj, info):
    return obj
