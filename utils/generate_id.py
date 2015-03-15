import uuid


def str_uuid():
    """
    Makes a unique 64-bit integer identifier integer and casts as a string
    """
    return str(uuid.uuid1().int >> 64)


def int_uuid():
    """
    Makes a unique 64-bit integer identifier integer
    """
    return uuid.uuid1().int >> 64