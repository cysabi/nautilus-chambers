"""Pydantic custom errors."""
from pydantic import PydanticValueError


class InvalidID(PydanticValueError):
    code = 'invalid_id'
    msg_template = 'Invalid ID, could not find {obj} object with ID: {id}'