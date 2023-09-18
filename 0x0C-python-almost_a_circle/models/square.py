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
    def size(self, value):
        """size setter"""
        """self.integer_validator("size", value)"""
        self.width = value
        self.height = value

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def __str__(self):
        """String representation of Square"""
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
            )

    def update(self, *args, **kwargs):
        """args and kwargs"""
        if args:
            update = ['id', 'size', 'x', 'y']

        for i, arg in enumerate(args):
            if i < len(update):
                setattr(self, update[i], arg)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
