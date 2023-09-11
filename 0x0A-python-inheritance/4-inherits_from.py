#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherits from a_class.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if obj is an instance of a class that inherits from a_class
    """
    cls = obj.__class__
    while cls is not None:
        if cls == a_class:
            return True
        cls = cls.__base__
    return False
