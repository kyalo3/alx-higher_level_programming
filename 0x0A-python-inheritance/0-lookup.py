#!/usr/bin/python3

def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)

class Example:
    def __init__(self):
        self.value = 42

    def method(self):
        return "Hello, World!"

obj = Example()
result = lookup(obj)
print(result)
