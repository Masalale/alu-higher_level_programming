#!/usr/bin/python3
"""Module that contains a function that lists all attributes and methods of an object"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object

    Args:
        obj: The object to inspect

    Returns:
        list: A list containing all attributes and methods of the object
    """
    return dir(obj)
