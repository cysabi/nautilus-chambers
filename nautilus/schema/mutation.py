"""Contains mutation resolvers."""
from ariadne import MutationType
from nautilus import utils

mutation_type = MutationType()


@mutation_type.field("createProfile")
def resolve_create_profile(*_, **kwargs):
    """mutation createProfile"""
    profile = utils.deep.update(
        utils.dbh.empty_profile(),
        kwargs['input']
    )
    utils.dbh.profiles.insert_one(profile)

    utils.logger.debug(f"createProfile | _id={profile['_id']} | discord={profile['discord']}")
    return {
        "status": True,
        "profile": profile,
        "error": None,
    }


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, **kwargs):
    """mutation updateProfile"""
    profile = utils.deep.update(
        utils.dbh.profiles.find_one(
            {'discord': kwargs['discord']}
        ),
        kwargs['input']
    )
    utils.dbh.profiles.replace_one({'discord': kwargs['discord']}, profile)

    utils.logger.debug(f"updateProfile | _id={profile['_id']} | discord={profile['discord']}")
    return {
        "status": True,
        "profile": profile,
        "error": None,
    }


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, **kwargs):
    """mutation deleteProfile"""
    profile = utils.dbh.profiles.find_one_and_delete({'discord': kwargs['discord']})

    utils.logger.debug(f"deleteProfile | _id={profile['_id']} | discord={profile['discord']}")
    return {
        "status": True,
        "profile": profile,
        "error": None,
    }
