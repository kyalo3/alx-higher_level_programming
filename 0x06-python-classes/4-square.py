#!/usr/bin/python3
"""creating a square class """


class Square():
    """ defining a square """

    def __init__(self, size=0):
        """ initializing the size attribute
        and setting it to private

        Args:
            size(int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        area = self.__size * self.__size
        return area
