"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import utils

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, discord):
    """query readProfile"""
    utils.logger.debug(f"readProfile | discord={discord}")
    payload = {}

    if not (error := utils.errors.check_for([utils.errors.missing], discord)):
        payload['profile'] = utils.dbh.find_profile(discord)
    else:
        payload['error'] = error

    payload['status'] = payload.get('profile', None) is not None
    return payload
