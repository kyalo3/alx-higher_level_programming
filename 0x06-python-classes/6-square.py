#!/usr/bin/python3
"""creating a square class """


class Square():
    """ defining a square """

    def __init__(self, size=0, position=(0, 0)):
        """ initializing the size attribute
        and setting it to private

        Args:
            size(int): the size of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position attribute."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(x, int) for x in value) or
            not all(x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
