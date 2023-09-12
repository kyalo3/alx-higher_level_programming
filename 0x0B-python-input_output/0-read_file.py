#!/usr/bin/python3
"""
a function that reads a text file and prints it to stdout:
"""


def read_file(filename="my_file_0.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass
