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
    def size(self):
        return self.__size

    def size(self, value):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
