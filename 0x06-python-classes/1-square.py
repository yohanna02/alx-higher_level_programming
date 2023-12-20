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
    def __init__(self, size):
        """This method initializes a new instance of Square.

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.__size = size
