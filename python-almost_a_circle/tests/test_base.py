#!/usr/bin/python3
"""
Unit tests for the Base model
"""
import unittest
import os
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Set up test cases"""
        Base._Base__nb_objects = 0

    def test_initialization(self):
        """Test Base initialization"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test to_json_string method"""
        test_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_string = Base.to_json_string([test_dict])
        self.assertTrue(isinstance(json_string, str))
        self.assertEqual(json.loads(json_string), [test_dict])

    def test_from_json_string(self):
        """Test from_json_string method"""
        test_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_string = json.dumps([test_dict])
        self.assertEqual(Base.from_json_string(json_string), [test_dict])

    def test_save_to_file(self):
        """Test save_to_file method"""
        # This is just a placeholder - adjust to your actual model implementation
        pass

    # Add more test methods as needed for other class methods


if __name__ == "__main__":
    unittest.main()
