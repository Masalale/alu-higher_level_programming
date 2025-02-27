#!/usr/bin/python3
# Square class with print capability


class Square:
    # Square class with display method

    def __init__(self, size=0):
        # Initialize square with optional size
        self.size = size

    @property
    def size(self):
        # Get the size of the square
        return self.__size

    @size.setter
    def size(self, value):
        # Set the size with validation
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # Return the current square area
        return self.__size ** 2

    def my_print(self):
        # Print the square using # characters
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
