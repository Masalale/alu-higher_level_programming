#!/usr/bin/python3
"""
Square module - implements Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class for representing squares

    Inherits from Rectangle since a square is a special case
    of a rectangle where width equals height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance

        Args:
            size: Size of the square (both width and height)
            x: X position of the square
            y: Y position of the square
            id: Identifier for this square
        """
        # Call the parent class constructor with id, x, y, width and height
        # For a square, width and height are both equal to size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square

        Updates both width and height to maintain a square shape.
        Uses the width validation from Rectangle.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square

        Returns:
            Formatted string with square dimensions and position
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
