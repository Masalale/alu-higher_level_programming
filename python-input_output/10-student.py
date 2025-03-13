#!/usr/bin/python3
"""
Student class definition with filtered attributes option
"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance
        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of a Student instance

        Args:
            attrs: List of attributes to include in the dictionary
                   If None, include all attributes
        Returns:
            Dictionary with the requested attributes
        """
        if attrs is None:
            return self.__dict__
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict
