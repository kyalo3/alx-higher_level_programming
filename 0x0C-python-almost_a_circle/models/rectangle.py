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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    def height(self):
        """height getter"""
        return self.__height

    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    def x(self):
        """x getter"""
        return self.__x

    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x m ust be >= 0")
        self.__x = value
