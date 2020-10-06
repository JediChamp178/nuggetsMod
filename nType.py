def xdict(keys: list, vals: list) -> dict:
    'Creates a dict by crossing keys and values'
    d = {}
    for key, val in keys, vals:
        d[key] = val
    return d
