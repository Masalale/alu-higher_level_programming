#!/usr/bin/python3
"""
Print square module - provides a function to print a square using # characters
"""


def print_square(size):
    """
    Prints a square made of # characters
    
    Args:
        size: The length of the square
        
    Raises:
        TypeError: If size is not an integer or is a negative float
        ValueError: If size is a negative integer
    """
    # Check if size is a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
        
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
        
    # Check if size is negative
    if size < 0:
        raise ValueError("size must be >= 0")
        
    # Print the square
    for _ in range(size):
        print("#" * size)
