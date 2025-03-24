#!/usr/bin/python3
"""
Base module - foundation for all classes in the project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string

        Args:
            list_dictionaries: List of dictionaries

        Returns:
            JSON string representation of the list of dictionaries
            "[]" if list_dictionaries is None or empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            cls: Class itself
            list_objs: List of instances who inherit from Base

        Note:
            The file will be overwritten if it already exists
        """
        # Create filename based on class name
        filename = cls.__name__ + ".json"

        # Handle None case by creating an empty list
        if list_objs is None:
            list_objs = []

        # Convert instances to dictionaries
        json_list = [obj.to_dictionary() for obj in list_objs]

        # Convert to JSON string
        json_str = cls.to_json_string(json_list)

        # Write to file
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation

        Args:
            json_string: String representing a list of dictionaries

        Returns:
            List represented by json_string
            Empty list if json_string is None or empty
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set

        Args:
            cls: Class itself
            **dictionary: Double pointer to a dictionary of attributes

        Returns:
            Instance with all attributes set
        """
        # Create dummy instance with minimum required attributes
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Width and height both 1
        elif cls.__name__ == "Square":
            dummy = cls(1)     # Size 1
        else:
            return None

        # Update the dummy instance with the real values
        dummy.update(**dictionary)
        
        return dummy
