from ariadne import ObjectType
from nautilus import dbh

meta_type = ObjectType("Meta")


@meta_type.field("discord")
def resolve_discord(obj, info):
    return dbh.get_field(obj, info)


@meta_type.field("twitter")
def resolve_twitter(obj, info):
    return dbh.get_field(obj, info)
