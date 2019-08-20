from ariadne import ObjectType
from nautilus import dbh

profile_type = ObjectType("Profile")


@profile_type.field("meta")
def resolve_meta(obj, info):
    return


@profile_type.field("status")
def resolve_status(obj, info):
    return
