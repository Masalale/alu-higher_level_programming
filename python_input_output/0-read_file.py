#!/usr/bin/python3
"""
Function to read a text file and print its contents
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
