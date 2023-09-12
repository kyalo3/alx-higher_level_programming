#!/usr/bin/python3
"""
a function that reads a text file and prints it to stdout:
"""


def write_file(filename="", text=""):

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
