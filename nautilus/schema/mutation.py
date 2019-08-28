from ariadne import ObjectType
from nautilus import dbh

mutation_type = ObjectType("Mutation")


@mutation_type.field("updateProfile")
def resolve_update_profile(obj, info, id, input):
    return {'status': True, 'profile': {'_id': id}}
