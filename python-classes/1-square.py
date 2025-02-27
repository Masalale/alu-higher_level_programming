#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Class that defines a square with a private size attribute"""

    def __init__(self, size):
        """Initialize a new Square instance with size

        Args:
            size: The size of the square (no type/value verification)
        """
        self.__size = size
