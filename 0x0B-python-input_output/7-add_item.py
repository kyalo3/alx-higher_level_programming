#!/usr/bin/python3
"""
a function that writes an Object to a text
file, using a JSON representation:
"""

import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
        
def save_to_json_file(my_obj, filename):
    """save an object using a JSON representation:"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
