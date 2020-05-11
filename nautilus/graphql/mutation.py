"""Contains mutation resolvers."""
from ariadne import MutationType
from nautilus import utils
from nautilus.validators import validate_profileinput

mutation_type = MutationType()


@mutation_type.field("createProfile")
def resolve_create_profile(*_, discord, profile):
    """mutation createProfile"""
    utils.logger.debug(f"createProfile | discord={discord}")
    errors = []
    if error := utils.errors.check_for([utils.errors.exists], discord):
        errors.append(error)
    profile, validation_errors = validate_profileinput(profile)
    if validation_errors:
        errors += validation_errors
    if not errors:
        return utils.dbh.insert_profile(discord, profile)

    return {"status": False, "errors": errors}


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, discord, profile):
    """mutation updateProfile"""
    utils.logger.debug(f"updateProfile | discord={discord}")
    errors = []
    if error := utils.errors.check_for([utils.errors.missing], discord):
        errors.append(error)
    profile, validation_errors = validate_profileinput(profile)
    if validation_errors:
        errors += validation_errors
    if not errors:
        return utils.dbh.update_profile(discord, profile)
    
    return {"status": False, "errors": errors}


@mutation_type.field("deleteProfile")
def resolve_delete_profile(*_, discord):
    """mutation deleteProfile"""
    utils.logger.debug(f"deleteProfile | discord={discord}")
    if not (error := utils.errors.check_for([utils.errors.missing], discord)):
        return utils.dbh.delete_profile(discord)

    return {"status": False, "errors": [error]}
