#!/usr/bin/python3
"""
class Rectangle that inherits from Base:
"""

from models.base import Base

class Rectangle(Base):


    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        """width getter"""
        return self.__width

    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("widt must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

