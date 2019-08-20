from ariadne import ObjectType
from nautilus import dbh

status_type = ObjectType("Status")


@status_type.field("ign")
def resolve_ign(obj, info):
    return "LeptoSpira"


@status_type.field("level")
def resolve_level(obj, info):
    return 104


@status_type.field("rank")
def resolve_rank(obj, info):
    return obj


@status_type.field("gear")
def resolve_gear(obj, info):
    return obj


@status_type.field("loadouts")
def resolve_loadouts(obj, info):
    return None
