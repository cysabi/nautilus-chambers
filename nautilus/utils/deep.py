"""Dictionary deep tools."""


def update(a, b):
    """Deepmerge dictionaries."""
    for key, value in b.items():
        if isinstance(value, dict):
            update(a[key], value)
        else:
            a[key] = value
    return a
