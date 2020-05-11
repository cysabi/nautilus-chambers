"""Contains query resolvers."""
from ariadne import QueryType
from nautilus import utils

query_type = QueryType()


@query_type.field("readProfile")
def resolve_read_profile(*_, discord):
    """query readProfile"""
    utils.logger.debug(f"readProfile | discord={discord}")
    if not (error := utils.errors.check_for([utils.errors.missing], discord)):
        return utils.dbh.find_profile(discord)

    return {"status": False, "errors": [error]}
