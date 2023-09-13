#!/usr/bin/python3

def write_file(filename="", text=""):
    """a function that reads a text file and prints it to stdout"""

    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(text)

    with open(filename, encoding="utf-8") as f:
        read = f.read()
        return len(read)
