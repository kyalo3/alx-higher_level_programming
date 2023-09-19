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

    @classmethod
    def create(cls, **dictionary):
        """Creates and returns an instance with attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """File to instances"""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """creating the create method"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """creating the load from file method"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, encoding="utf-8")as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))
        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file csv method"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dict = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dict = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dict[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dict[:])

        with open(filename, 'w', encoding="utf-8") as f:
            writ = csv.writer(f)
            writ.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
