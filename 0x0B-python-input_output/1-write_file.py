#!/usr/bin/python3
"""
a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """a function that reads a text file and prints it to stdout"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
