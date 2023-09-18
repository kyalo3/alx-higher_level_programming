#!/usr/bin/python3
"""
class Rectangle that inherits from Base:
"""

from models.base import Base


class Rectangle(Base):
    """a function"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """new public method - area"""
    def area(self):
        """calculates the area"""
        return self.__width * self.__height

    def display(self):
        """display the obj by printing to stdout"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Overrides the default __str__ method"""
        str_self = f("[Rectangle] ({self.id}) "
                     f"{self.__x}/{self.__y} - "
                     f"{self.__width}/{self.__height}")

        return (str_self)

    def update(self, *args, **kwargs):
        """update the attributes of Rectangle:"""
        if args:
            update = ['id', 'width', 'height', 'x', 'y']

            for i, arg in enumerate(args):
                if i < len(update):
                    setattr(self, update[i], arg)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
