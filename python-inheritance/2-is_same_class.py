#!/usr/bin/python3
"""Module containing function to check exact class instance"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
