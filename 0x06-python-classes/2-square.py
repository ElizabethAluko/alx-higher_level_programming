#!/usr/bin/python3


"""Define a Square class"""


class Square:
    """A square has four equal sides"""

    def __init__(self, size=0):
        """Create a new Square object.


        Args:
            size (int): The size of the new square object
        """
        try:
            int size
            if size >= 0:
                continue
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >=0")
        finally:
            self.__size = size
