#!/usr/bin/python3
class LockedClass:
    """ class Lockedclass"""
    __slots__ = ('first_name',)


    def __init__(self):
        ""
        if hasattr(self, 'first_name'):
            self.first_name = None

    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
