#!/usr/bin/python3
"""
a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or inherited from a_class.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if obj is an instance of a_class or inherited from it, False otherwise    """
    return isinstance(obj, a_class)
