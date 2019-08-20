from ariadne import QueryType
from nautilus import dbh

query_type = QueryType()


@query_type.field("profiles")
def resolve_profiles(obj, info, **kwargs):
    return kwargs


@query_type.field("test")
def resolve_profiles(obj, info):
    return
