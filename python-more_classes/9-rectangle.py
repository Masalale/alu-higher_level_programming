#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """Rectangle with width, height and additional features"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return rectangle perimeter (0 if width/height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rectangle with larger area (rect_1 if equal)"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a square Rectangle with equal width and height"""
        return cls(size, size)

    def __str__(self):
        """Return printable rectangle representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rect = []
        for i in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Return string representation for recreation with eval()"""
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """Print message when rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
