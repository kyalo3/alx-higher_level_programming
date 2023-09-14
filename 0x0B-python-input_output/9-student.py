#!/usr/bin/python3
"""
class Student that defines a student
"""

import json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return {
            "first_name": self.first_name,
            "last_name": self.first_name.split()[0],
            "age": self.age
            }"""
        return self.__dict__
