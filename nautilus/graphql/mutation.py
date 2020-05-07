"""Contains mutation resolvers."""
from ariadne import MutationType
from nautilus import utils

mutation_type = MutationType()


@mutation_type.field("createProfile")
def resolve_create_profile(*_, discord, profile):
    """mutation createProfile"""
    utils.logger.debug(f"createProfile | discord={discord}")
    status, profile = utils.dbh.insert_profile(discord, profile)
    return {
        "status": status,
        "profile": profile,
        "error": None,
    }


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, discord, profile):
    """mutation updateProfile"""
    utils.logger.debug(f"updateProfile | discord={discord}")
    status, profile = utils.dbh.update_profile(discord, profile)
    return {
        "status": status,
        "profile": profile,
        "error": None,
    }


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, discord):
    """mutation deleteProfile"""
    utils.logger.debug(f"deleteProfile | discord={discord}")
    status, profile = utils.dbh.delete_profile(discord)
    return {
        "status": status,
        "profile": profile,
        "error": None,
    }
