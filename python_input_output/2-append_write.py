#!/usr/bin/python3
"""
Function to append text to a file
"""


def append_write(filename="", text=""):
    """
    Appends text to a file, creates it if needed.
    Returns number of chars written.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
