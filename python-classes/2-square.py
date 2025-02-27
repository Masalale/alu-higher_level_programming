#!/usr/bin/python3
# Square class with size validation


class Square:
    # Square with size validation - checks if it's a proper square

    def __init__(self, size=0):
        # Check if size is an int
        if type(size) is not int:
            raise TypeError("size must be an integer")
        # Make sure size isn't negative
        if size < 0:
            raise ValueError("size must be >= 0")
            
        # Seems good, let's set it
        self.__size = size
