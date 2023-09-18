#!/usr/bin/python3
"""
create a class - Base
"""

import os
import unittest
from tests.test_models import test_base


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
