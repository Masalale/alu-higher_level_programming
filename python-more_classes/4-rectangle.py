#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle with width and height attributes"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle

        Returns:
        int: The perimeter (2 * (width + height)) or 0 if width/height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle

        Returns:
            str: Rectangle represented with # characters or empty string if
                width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Return a string representation to recreate the rectangle

        Returns:
            str: String that can be used with eval() to recreate the instance
        """
        return f"Rectangle({self.__width}, {self.__height})"
