"""Contains mutation resolvers."""
from ariadne import MutationType
from nautilus import logger, dbh

mutation_type = MutationType()


@mutation_type.field("createProfile")
def resolve_create_profile(*_, **kwargs):
    """mutation createProfile"""
    profile = dbh.empty_profile.copy()
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = dbh.errors['missing']

    # All Good
    else:
        profile.update(kwargs['input'])
        payload['profile'] = dbh.profiles.insert_one(profile)
        logger.debug(payload['profile']["_id"])

    payload['status'] = True if not payload.get('error') else False
    return payload


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, **kwargs):
    """mutation updateProfile"""
    profile = dbh.profiles.find_one(kwargs['discord'])
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = dbh.errors['missing']

    # All Good
    else:
        profile.update(kwargs['input'])
        payload['profile'] = dbh.profiles.replace_one(kwargs['discord'], profile)

    payload['status'] = True if not payload.get('error') else False
    return payload


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, **kwargs):
    """mutation deleteProfile"""
    profile = dbh.profiles.find_one(kwargs['discord'])
    payload = {}

    # Check for errors
    if profile is None:
        payload['error'] = dbh.errors['missing']

    # All Good
    else:
        dbh.profiles.delete_one(kwargs['discord'])

    payload['status'] = True if not payload.get('error') else False
    return payload
