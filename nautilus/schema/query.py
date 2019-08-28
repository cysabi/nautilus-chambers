from ariadne import QueryType
from nautilus import dbh

query_type = QueryType()


@query_type.field("profile")
def resolve_profiles(obj, info, **kwargs):
    kwargs['_id'] = kwargs.pop('id')
    return kwargs
