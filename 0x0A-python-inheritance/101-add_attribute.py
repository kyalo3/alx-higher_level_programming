#!/usr/bin/python3
"""
a function that adds a new attribute to
an object if it’s possible
"""


def add_attribute(obj, attribute, value):
    """he object can’t have new attribute"""

    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__')
       and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
