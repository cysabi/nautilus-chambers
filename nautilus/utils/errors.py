"""Errors to show the user when their graphql request isn't working."""
from . import dbh


def check_for(errors, discord):
    """Check for errors."""
    for err in errors:
        if error := err(discord):
            return error


def missing(discord):
    """Return an error if profile is missing."""
    return False if dbh.profiles.count_documents({"_id": discord}) else "Profile not found."


def exists(discord):
    """Return an error if profile exists."""
    return False if not dbh.profiles.count_documents({"_id": discord}) else "Profile already exists."
