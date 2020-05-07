"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import utils

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, discord):
    """query readProfile"""
    utils.logger.debug(f"readProfile | discord={discord}")
    profile = utils.dbh.find_profile(discord)
    error = None if profile else "Unable to access profile. Either the profile doesn't exist or you do not have access to it."
    return {
        "status": profile is not None,
        "profile": profile,
        "error": error,
    }
