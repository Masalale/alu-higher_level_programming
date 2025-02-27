#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle

        Returns:
            str: Rectangle description in the format [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
