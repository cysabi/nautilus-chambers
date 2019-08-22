from ariadne import ObjectType
from nautilus import dbh

abilities_type = ObjectType("Abilities")


@abilities_type.field("main")
def resolve_main(obj, info):
    return dbh.get_field(obj, info)


@abilities_type.field("subs")
def resolve_subs(obj, info):
    return dbh.get_field(obj, info)
