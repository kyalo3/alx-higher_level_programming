#!/usr/bin/python3
"""
class Rectangle that defines a rectangle by:
    Private instance attribute: width
    Private instance attribute: height
"""


class Rectangle:
    """Class Rectangle """
    def __init__(self, width=0, height=0):
        """Instantiate class Rectangle: width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get rectangle:width"""
        return self.__width

    @property
    def height(self):
        """Get rectangle:height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set a new rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set a new rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the reactangle"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
