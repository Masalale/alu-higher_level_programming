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

    def update(self, *args, **kwargs):
        """Update the square attributes

        Args:
            *args: Variable length argument list
                1st argument should be id
                2nd argument should be size
                3rd argument should be x
                4th argument should be y
            **kwargs: Variable length keyword argument dictionary
                Each key represents an attribute to update
        """
        # If args exists and is not empty, use positional arguments
        if args and len(args) > 0:
            # Map attributes to their positions in args
            attrs = ['id', 'size', 'x', 'y']

            # Update each attribute based on position in args
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if i == 1:  # size handling
                        setattr(self, attrs[i], arg)
                    else:  # direct attribute setting
                        setattr(self, attrs[i], arg)
        # Otherwise use keyword arguments
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square

        Returns:
            Dictionary containing all properties of the Square instance
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
