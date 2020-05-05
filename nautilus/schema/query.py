"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import utils

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, discord):
    """query readProfile"""
    profile = utils.dbh.find_profile(discord)
    utils.logger.debug(f"readProfile | discord={discord}")
    return {
        "status": profile is not None,
        "profile": profile,
        "error": None,
    }
