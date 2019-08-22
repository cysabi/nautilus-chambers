from ariadne import ObjectType
from nautilus import dbh

wear_type = ObjectType("Wear")


@wear_type.field("name")
def resolve_name(obj, info):
    return dbh.get_field(obj, info)


@wear_type.field("abilities")
def resolve_abilities(obj, info):
    return dbh.pass_field(obj, info)
