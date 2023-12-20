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
        self.size(size)

    @property
    def size(self):
        """Getter for __size attribute.

        Args:
            None

        Returns:
            The value of __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size attribute.

        Args:
            value (int): value to set __size to

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This method calculates the area of the square.

        Args:
            None

        Returns:
            The area of the square.
        """
        return self.__size ** 2
