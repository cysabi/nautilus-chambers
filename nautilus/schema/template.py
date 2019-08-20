from ariadne import ObjectType
from nautilus import dbh

CLASSTYPE_type = ObjectType("CLASS")


@CLASSTYPE_type.field("FIELD")
def resolve_FIELD(obj, info):
    return FIELDRET


@CLASSTYPE_type.field("FIELD")
def resolve_FIELD(obj, info):
    return FIELDRET
