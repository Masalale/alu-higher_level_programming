#!/usr/bin/python3
"""
Unit tests for Square class
"""
import unittest
import io
from unittest.mock import patch
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_initialization(self):
        """Test Square initialization"""
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(10, 2, 3, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_size_property(self):
        """Test size property validation"""
        s = Square(10)
        with self.assertRaises(TypeError):
            s.size = "invalid"
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaises(ValueError):
            s.size = -1
        s.size = 15
        self.assertEqual(s.size, 15)
        self.assertEqual(s.width, 15)
        self.assertEqual(s.height, 15)

    def test_x_property(self):
        """Test x property validation"""
        s = Square(10)
        with self.assertRaises(TypeError):
            s.x = "invalid"
        with self.assertRaises(ValueError):
            s.x = -1
        s.x = 0  # Should not raise exception
        s.x = 30
        self.assertEqual(s.x, 30)

    def test_y_property(self):
        """Test y property validation"""
        s = Square(10)
        with self.assertRaises(TypeError):
            s.y = "invalid"
        with self.assertRaises(ValueError):
            s.y = -1
        s.y = 0  # Should not raise exception
        s.y = 30
        self.assertEqual(s.y, 30)

    def test_str(self):
        """Test __str__ method"""
        s1 = Square(4, 2, 1, 12)
        expected_str = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s1), expected_str)

    def test_update_args(self):
        """Test update method with positional arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(89, 2)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        s1.update(89, 2, 3)
        self.assertEqual(s1.x, 3)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.y, 4)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        s1 = Square(10, 10, 10, 10)
        s1.update(id=1)
        self.assertEqual(s1.id, 1)
        s1.update(size=7, id=89)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        s1.update(y=3, size=15, x=12)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.size, 15)
        self.assertEqual(s1.x, 12)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s1 = Square(10, 2, 1, 5)
        expected_dict = {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_dict)

    def test_area(self):
        """Test area calculation (inherited from Rectangle)"""
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)
        s2 = Square(8, 0, 0, 12)
        self.assertEqual(s2.area(), 64)

    def test_display(self):
        """Test display method (inherited from Rectangle)"""
        # Test simple display
        s1 = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test display with offsets
        s2 = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            s2.display()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
