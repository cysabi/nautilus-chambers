from ariadne import ObjectType
from nautilus import dbh

rank_type = ObjectType("Rank")


@rank_type.field("sz")
def resolve_sz(obj, info):
    return "S+9"


@rank_type.field("rm")
def resolve_rm(obj, info):
    return "X2144"


@rank_type.field("tc")
def resolve_tc(obj, info):
    return "A-"


@rank_type.field("cb")
def resolve_cb(obj, info):
    return "B+"


@rank_type.field("sr")
def resolve_sr(obj, info):
    return "Profreshional"
