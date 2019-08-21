from ariadne import ObjectType
from nautilus import dbh

profile_type = ObjectType("Profile")


@profile_type.field("id")
def resolve_id(obj, info):
    return 1


@profile_type.field("meta")
def resolve_meta(obj, info):
    return obj


@profile_type.field("status")
def resolve_status(obj, info):
    return obj
