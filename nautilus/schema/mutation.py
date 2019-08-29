from ariadne import ObjectType
from nautilus import dbh

mutation_type = ObjectType("Mutation")


@mutation_type.field("updateProfile")
def resolve_update_profile(*_, **kwargs):
    filter = {'_id': kwargs['id']}

    profile = dbh.update_profile(dbh.col.find_one(filter), kwargs['input'])
    dbh.col.replace_one(filter, profile)

    return {'status': True, 'profile': filter}
