"""Pydantic custom errors."""
from pydantic import PydanticValueError


class InvalidID(PydanticValueError):
    code = 'invalid_object_id'
    msg_template = 'Invalid object ID, could not find {obj} object with ID: {id}'
