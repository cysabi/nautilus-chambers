from pydantic import ValidationError

from . import errors
from . import models


def validate_profileinput(profile_raw):
    """Validate ProfileInput user input data."""
    profile, errs = None, []
    try:
        profile = models.ProfileInput(**profile_raw).dict()
    except ValidationError as e:
        errs = e.errors()
    return profile, errs
