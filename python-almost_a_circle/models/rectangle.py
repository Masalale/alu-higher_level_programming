#!/usr/bin/python3
"""
Rectangle module - implements Rectangle class that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class for representing rectangles

    Inherits from the Base class and adds width, height,
    and position attributes with validation.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance

        Args:
            width: Width of the rectangle
            height: Height of the rectangle
            x: X position of the rectangle
            y: Y position of the rectangle
            id: Identifier for this rectangle
        """
        # Call the parent class constructor with id
        super().__init__(id)

        # Set each attribute through properties for validation
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle with validation"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle with validation"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            The area value (width * height)
        """
        return self.width * self.height

    def display(self):
        """Display the rectangle using # characters

        Prints a visual representation of the rectangle
        using # symbols, taking into account x and y coordinates
        for positioning.
        """
        # Print y offset as empty lines
        for _ in range(self.y):
            print()

        # For each row of the rectangle
        for _ in range(self.height):
            # Print x offset as spaces, then the row of # symbols
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle

        Returns:
            Formatted string with rectangle dimensions and position
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
