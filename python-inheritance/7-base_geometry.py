#!/usr/bin/python3
"""Module defining a BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Calculate area of a geometry shape

        Raises:
            Exception: This method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer

        Args:
            name (str): The name of the value being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
