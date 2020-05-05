"""Dictionary deep tools."""


def update(a, b):
    """Deepmerge dictionaries."""
    b = b.copy()
    for key, value in b.items():
        if not any(isinstance(i, dict) for i in b.values()):
            a.update(b)
        else:
            update(a[key], value)
