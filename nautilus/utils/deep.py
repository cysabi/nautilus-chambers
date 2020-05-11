"""Dictionary deep tools."""


def update(d, u):
    """Deepmerge 2 dicts."""
    if not isinstance(d, dict):
        return u
    for k, v in u.items():
        if isinstance(v, dict):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d