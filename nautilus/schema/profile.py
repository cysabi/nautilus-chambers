from ariadne import ObjectType
from nautilus import dbh

profile_type = ObjectType("Profile")


@profile_type.field("_id")
def resolve_id(obj, info):
    return dbh.get_field(obj, info)


@profile_type.field("meta")
def resolve_meta(obj, info):
    return dbh.pass_field(obj, info)


@profile_type.field("status")
def resolve_status(obj, info):
    return dbh.pass_field(obj, info)
