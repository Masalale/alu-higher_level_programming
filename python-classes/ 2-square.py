#!/usr/bin/python3
# Module that defines a Square class


class Square:
    # Class that defines a square with a private size attribute

    def __init__(self, size=0):
        # Initialize a new Square instance with optional size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
