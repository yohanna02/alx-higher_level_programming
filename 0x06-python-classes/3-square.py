#!/usr/bin/python3
"""
This module defines a simple Square class.

Class:
    squre: represents a square

Attributes:
    None
"""


class Square:
    """This class represents a square.

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """This method initializes a new instance of Square.

        Args:
            size (int, optional): size of a side of the square, Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This method calculates the area of the square.

        Args:
            None

        Returns:
            The area of the square.
        """
        return self.__size ** 2
