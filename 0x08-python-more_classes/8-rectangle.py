#!/usr/bin/python3
""" An empty class recrangle that defines a rectangle """


class Rectangle:
    """ define the rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instatiating an object
        Args:
        width (int): width of the rectangle object
        """
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """use getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """use setter to set the value
        Args:
        value (int): width value
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height
        Args:
        value (int): height
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """initializing area"""
        return self.__width*self.__height

    def perimeter(self):
        """defining perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """converting to string"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """getting a string representation"""
        string = 'Rectangle(' + str(self.__width) + ', ' + \
            str(self.__height) + ')'
        return string

    def __del__(self):
        Rectangle.number_of_instances -= 1
        output = "Bye rectangle..."
        print(output)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        x = rect_1.area()
        y = rect_2.area()
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if x >= y:
            return rect_1
        else:
            return rect_2
