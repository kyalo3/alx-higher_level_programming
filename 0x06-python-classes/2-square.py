#!/usr/bin/python3
"""creating a square class """


class Square():
    """ defining a square """

    def __init__(self, size=0):
        """ initializing the size attribute """
        if (type(size) is not int):
            raise TypeError("size is not integer")
        elif (size  < 0):
             raise ValueError("size must be >= 0")
        self.__size = size
