#!/usr/bin/python3
"""Module that defines MyList class inheriting from list"""


class MyList(list):
    """A class that inherits from list and adds sorting print capability"""

    def print_sorted(self):
        """Prints the list in ascending sorted order

        All elements are assumed to be integers.
        """
        print(sorted(self))
