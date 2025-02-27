#!/usr/bin/python3
"""Module containing function to check class inheritance"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from specified class

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj inherits from a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
