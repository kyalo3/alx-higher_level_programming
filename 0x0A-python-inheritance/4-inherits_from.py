#!/usr/bin/python3
"""
a function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherits from a_class.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if obj is an instance of a class that inherits from a_class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
