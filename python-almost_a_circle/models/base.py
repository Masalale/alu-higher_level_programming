#!/usr/bin/python3
"""
Base module - foundation for all classes in the project
"""


class Base:
    """Base class for managing object IDs

    This class handles ID assignment for all derived classes,
    helping to avoid duplicate code and reduce bugs.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Set up a new instance with a unique ID

        Args:
            id: Optional identifier value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
