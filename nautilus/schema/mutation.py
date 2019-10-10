from ariadne import ObjectType
from nautilus import dbh
import copy

mutation_type = ObjectType("Mutation")


@mutation_type.field("createProfile")
def resolve_create_profile(*_, **kwargs):
    payload = {}
    profile = copy.deepcopy(dbh.empty_profile)
    dbh.deepmerge(profile, kwargs['input'])

    # Check for errors
    if profile is None:
        payload['error'] = dbh.errors['missing']

    # All Good
    else:
        payload['profile'] = dbh.col.find_one(
            {"_id": dbh.col.insert_one(profile).inserted_id}
        )
        print(payload['profile']["_id"])
    payload['status'] = True if not payload.get('error') else False

    return payload


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, **kwargs):
    payload = {}
    profile = dbh.col.find_one(kwargs['discord'])
    dbh.deepmerge(profile, kwargs['input'])

    # Check for errors
    if profile is None:
        payload['error'] = dbh.errors['missing']

    # All Good
    else:
        payload['profile'] = dbh.col.replace_one(kwargs['discord'], profile)

    payload['status'] = True if not payload.get('error') else False

    return payload


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, **kwargs):
    payload = {}
    profile = dbh.col.find_one(kwargs['discord'])

    # Check for errors
    if profile is None:
        payload['error'] = dbh.errors['missing']

    # All Good
    else:
        dbh.col.delete_one(kwargs['discord'])

    payload['status'] = True if not payload.get('error') else False

    return payload
