"""Contains mutation resolvers."""
from ariadne import MutationType
from nautilus import utils

mutation_type = MutationType()


@mutation_type.field("createProfile")
def resolve_create_profile(*_, **kwargs):
    """mutation createProfile"""
    profile = utils.dbh.empty_profile.copy()
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = utils.dbh.errors['missing']

    # All Good
    else:
        profile.update(kwargs['input'])
        payload['profile'] = utils.dbh.profiles.insert_one(profile)
        utils.logger.debug("createProfile ran. ID: " + payload['profile']["_id"])

    payload['status'] = True if not payload.get('error') else False
    return payload


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, **kwargs):
    """mutation updateProfile"""
    profile = utils.dbh.profiles.find_one(kwargs['discord'])
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = utils.dbh.errors['missing']

    # All Good
    else:
        profile.update(kwargs['input'])
        payload['profile'] = utils.dbh.profiles.replace_one(kwargs['discord'], profile)
        utils.logger.debug("updateProfile ran. ID: " + payload['profile']["_id"])

    payload['status'] = True if not payload.get('error') else False
    return payload


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, **kwargs):
    """mutation deleteProfile"""
    profile = utils.dbh.profiles.find_one(kwargs['discord'])
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = utils.dbh.errors['missing']

    # All Good
    else:
        profile = utils.dbh.profiles.delete_one(kwargs['discord'])
        utils.logger.debug("deleteProfile ran. ID: " + profile["_id"])

    payload['status'] = True if not payload.get('error') else False
    return payload
