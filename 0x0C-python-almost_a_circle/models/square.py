#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor: """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def self(self, value):
        """size setter"""
        self.integer_validator("size", value)
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of Square"""
        sq_str = (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}") 
        return sq_str
