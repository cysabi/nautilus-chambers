from ariadne import ObjectType
from nautilus import dbh

rank_type = ObjectType("Rank")


@rank_type.field("sz")
def resolve_sz(obj, info):
    return dbh.get_field(obj, info)


@rank_type.field("rm")
def resolve_rm(obj, info):
    return dbh.get_field(obj, info)


@rank_type.field("tc")
def resolve_tc(obj, info):
    return dbh.get_field(obj, info)


@rank_type.field("cb")
def resolve_cb(obj, info):
    return dbh.get_field(obj, info)


@rank_type.field("sr")
def resolve_sr(obj, info):
    return dbh.get_field(obj, info)
