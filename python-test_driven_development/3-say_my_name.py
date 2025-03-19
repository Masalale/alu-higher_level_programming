#!/usr/bin/python3
"""
Say my name module - provides a function to print a name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a full name in the format 'My name is <first_name> <last_name>'
    
    Args:
        first_name: The first name, must be a string
        last_name: The last name, defaults to empty string
        
    Raises:
        TypeError: If either name is not a string
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the name
    print("My name is {} {}".format(first_name, last_name))
