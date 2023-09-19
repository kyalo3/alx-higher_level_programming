#!/usr/bin/python3
"""
create a class - Base
"""

import json
import os.path
import csv
import unittest


class Base:
    """private class attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instance/ attributes of base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the JSON string representation to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json.dump([obj.to_dictionary() for obj in list_objs], file)
