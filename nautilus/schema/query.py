"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import dbh

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, **kwargs):
    """query readProfile"""
    try:
        return {
            'status': True,
            'profile': dbh.profiles.find_one({"discord": kwargs["discord"]})
        }
    except Exception as exc:
        return {'status': False, 'error': exc, 'profile': None}
