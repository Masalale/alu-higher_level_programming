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
