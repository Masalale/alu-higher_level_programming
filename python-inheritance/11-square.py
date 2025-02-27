#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square instance

        Args:
            size (int): Size of the square sides

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the square

        Returns:
            str: Square description in the format [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
