#!/usr/bin/python3
"""Define a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inheritd ftom base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate the rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the new value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the new value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set the new value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set the new value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """Displays rectangle object with '#' in stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print(' ')
        for i in range(self.height):
            for w in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                if j == self.width - 1:
                    print('#')
                else:
                    print('#', end='')

    def __str__(self):
        """Return defined string representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height))

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""
        if args and len(args) != 0:
            i = 0

            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(
                                self.width,
                                self.height,
                                self.x,
                                self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(
                                self.width,
                                self.height,
                                self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns dictionary representatio"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
