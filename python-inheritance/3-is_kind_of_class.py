#!/usr/bin/python3
"""Module containing function to check class instance and inheritance"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of class or its subclasses"""
    return isinstance(obj, a_class)
