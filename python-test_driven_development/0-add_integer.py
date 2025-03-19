#!/usr/bin/python3
"""
Add integer module - provides function to add two numbers
"""


def add_integer(a, b=98):
    """
    Add two integers together

    Both numbers must be integers or floats
    Floats are converted to integers before addition
    Returns the integer sum of a and b
    """
    # Check if inputs are valid numbers
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert to integers and return sum
    return int(a) + int(b)
