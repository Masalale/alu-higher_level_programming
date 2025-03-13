#!/usr/bin/python3
"""
Student class definition
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

    def to_json(self):
        """
        Returns dictionary representation of a Student instance
        """
        return self.__dict__
