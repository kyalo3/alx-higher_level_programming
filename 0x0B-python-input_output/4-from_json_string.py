#!/usr/bin/python3
"""
a function that returns an object
"""

import json


def from_json_string(my_str):
    """returns an object"""
    return json.loads(my_str)
