#!/usr/bin/python3
"""Module containing function to check class instance and inheritance"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of class or its subclasses

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is instance of a_class or its subclasses,
              False otherwise
    """
    return isinstance(obj, a_class)