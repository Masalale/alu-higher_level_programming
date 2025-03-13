#!/usr/bin/python3
"""
Function to convert Python object to JSON string
"""
import json


def to_json_string(my_obj):
    """
    Returns JSON representation of an object.
    """
    return json.dumps(my_obj)
