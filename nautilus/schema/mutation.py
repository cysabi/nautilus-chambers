"""Contains mutation resolvers."""
from ariadne import MutationType
from nautilus import utils

mutation_type = MutationType()


@mutation_type.field("createProfile")
def resolve_create_profile(*_, discord, profile):
    """mutation createProfile"""
    status, profile = utils.dbh.insert_profile(discord, profile)
    utils.logger.debug(f"createProfile | discord={discord}")
    return {
        "status": status,
        "profile": profile,
        "error": None,
    }


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, discord, profile):
    """mutation updateProfile"""
    status, profile = utils.dbh.update_profile(discord, profile)
    utils.logger.debug(f"updateProfile | discord={discord}")
    return {
        "status": True,
        "profile": profile,
        "error": None,
    }


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, discord):
    """mutation deleteProfile"""
    status, profile = utils.dbh.delete_profile(discord)
    utils.logger.debug(f"deleteProfile | discord={discord}")
    return {
        "status": True,
        "profile": profile,
        "error": None,
    }
