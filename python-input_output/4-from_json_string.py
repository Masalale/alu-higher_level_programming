#!/usr/bin/python3
"""
Function to convert JSON string to Python object
"""
import json


def from_json_string(my_str):
    """
    Returns Python data structure from JSON string.
    """
    return json.loads(my_str)
