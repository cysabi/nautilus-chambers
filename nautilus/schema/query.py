"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import utils

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, **kwargs):
    """query readProfile"""
    profile = utils.dbh.profiles.find_one({'discord': kwargs['discord']})

    utils.logger.debug(f"queryProfile | _id={profile['_id']} | discord={profile['discord']}")
    return {
        "status": True,
        "profile": profile,
        "error": None,
    }
