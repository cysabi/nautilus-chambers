from ariadne import ObjectType
from nautilus import dbh

mutation_type = ObjectType("Mutation")


@mutation_type.field("createProfile")
def resolve_update_profile(*_, **kwargs):
    return dbh.create_profile(kwargs)


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, **kwargs):
    return dbh.update_profile(kwargs)


@mutation_type.field("deleteProfile")
def resolve_update_profile(*_, **kwargs):
    return dbh.delete_profile(kwargs)
