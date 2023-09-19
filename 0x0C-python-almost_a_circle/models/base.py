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
        list_dict = []  # Add this line to define the list_dict
        for i in range(len(list_objs)):
            list_dict.append(list_objs[i].to_dictionary())

        with open(filename, 'w', encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(list_dict))

    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
