from pydantic import ValidationError

from . import errors
from . import models


def validate_profileinput(profile):
    """Validate ProfileInput user input data."""
    payload = {
        'profile': None,
        'error': None
    }
    try:
        payload['profile'] = models.ProfileInput(**profile)
    except ValidationError as e:
        payload['error'] = e.errors()[0]['msg']
    return {**payload, 'status': not payload['error']}
