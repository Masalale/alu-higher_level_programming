#!/usr/bin/python3
"""Module that defines a Square class with printing capability."""


class Square:
    """Square class with methods to set/get size, calculate area and print."""

    def __init__(self, size=0):
        """Initialize a new Square instance with optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print a visual representation of the square using # characters."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
