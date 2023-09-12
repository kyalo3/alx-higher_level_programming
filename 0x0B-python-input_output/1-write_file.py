#!/usr/bin/python3
"""
a function that reads a text file and prints it to stdout:
"""


def write_file(filename="my_first_file.txt", text="This School is so cool!\n"):

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)


"""write_file('my_first_file.txt', 'This School is so cool!\n')"""
