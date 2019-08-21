from ariadne import ObjectType
from nautilus import dbh

meta_type = ObjectType("Meta")


@meta_type.field("discord")
def resolve_discord(obj, info):
    return 571494333090496514


@meta_type.field("twitter")
def resolve_twitter(obj, info):
    return None
