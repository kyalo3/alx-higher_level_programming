#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    prints a sorted list
    """
    def print_sorted(self):
        """
        printing the list
        """
        print(sorted(self))
