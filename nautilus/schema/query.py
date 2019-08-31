from ariadne import QueryType
from nautilus import dbh

query_type = QueryType()


@query_type.field("readProfile")
def resolve_profiles(*_, **kwargs):
    kwargs = dbh.replace_id(kwargs)

    if dbh.doc_exists(kwargs):
        return {'status': True, 'profile': kwargs}

    return {
        'status': False,
        'error':
        'Profile either doesn\'t exist, or you do not have permission to see it',
        'profile': None
    }
