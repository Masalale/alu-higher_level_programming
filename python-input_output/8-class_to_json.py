#!/usr/bin/python3
"""
Function to convert class to JSON serializable dictionary
"""


def class_to_json(obj):
    """
    Returns dictionary description of an object for JSON serialization
    Args:
        obj: instance of a class with serializable attributes
    Returns:
        Dictionary representation of the object
    """
    return obj.__dict__
