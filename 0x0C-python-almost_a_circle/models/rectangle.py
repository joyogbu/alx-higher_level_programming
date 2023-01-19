#!/usr/bin/python3
"""class rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """representing the class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiating the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """use getter to retrieve the width"""
        return self.__width

    @width.setter
    def width(self, val):
        """use setter to set the width"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """use getter to get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """use setter to set the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """use getter to get x"""
        return self.__x

    @x.setter
    def x(self, val):
        """use setter to set x"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """use getter to get y"""
        return self.__y

    @y.setter
    def y(self, valu):
        """using setter to set the value"""
        if type(valu) != int:
            raise TypeError("y must be an integer")
        if valu < 0:
            raise ValueError("y must be >= 0")
        self.__y = valu

    def area(self):
        """defing the function for area of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """defining display to print rectangle
        """
        string = "#"
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print(string, end="")
            print()

    def update(self, *args, **kwargs):
        """updating the rectangle object"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                else:
                    self.y = arg
        if kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of the
        rectangle class"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """string representation of the rectangle object"""
        string = "[" + self.__class__.__name__ + "]" + " (" + \
            str(self.id) + ") " + str(self.__x) + "/" + \
            str(self.__y) + " - " + str(self.__width) + "/" + \
            str(self.__height)
        return (string)
