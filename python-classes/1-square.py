#!/usr/bin/python3
# Square class definition with private size


class Square:
    # Class that defines a square

    def __init__(self, size):
        # Initialize new Square with size
        # size: size of the square (no type checking here)
        self.__size = size
