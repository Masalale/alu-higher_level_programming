#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
import io
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def setUp(self):
        """Reset Base.__nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_initialization(self):
        """Test Rectangle initialization"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 20, 3, 4, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_width_property(self):
        """Test width property validation"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.width = -1
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_height_property(self):
        """Test height property validation"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.height = -1
        r.height = 30
        self.assertEqual(r.height, 30)

    def test_x_property(self):
        """Test x property validation"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.x = -1
        r.x = 0  # Should not raise exception
        r.x = 30
        self.assertEqual(r.x, 30)

    def test_y_property(self):
        """Test y property validation"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.y = -1
        r.y = 0  # Should not raise exception
        r.y = 30
        self.assertEqual(r.y, 30)

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        """Test display method"""
        # Test simple display
        r1 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test display with offsets
        r2 = Rectangle(2, 2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), expected_str)

    def test_update_args(self):
        """Test update method with positional arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=1)
        self.assertEqual(r1.id, 1)
        r1.update(width=2, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        r1.update(y=3, width=15, x=12)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 15)
        self.assertEqual(r1.x, 12)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9, 5)
        expected_dict = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
