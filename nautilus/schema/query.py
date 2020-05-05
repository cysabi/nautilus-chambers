"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import utils

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, **kwargs):
    """query readProfile"""
    profile = utils.dbh.profiles.find_one({"discord": kwargs["discord"]})
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = utils.dbh.errors['missing']

    # All Good
    else:
        payload['profile'] = profile
        utils.logger.debug("readProfile ran. ID: " + payload['profile']["_id"])

    payload['status'] = True if not payload.get('error') else False
    return payload
