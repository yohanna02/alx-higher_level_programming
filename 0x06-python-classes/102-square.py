#!/usr/bin/python3
"""
This module defines a simple Square class.

Class:
    Square: Represents a square.

Attributes:
    None
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int, optional): The size of the square.
            Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            float or int: The square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare if two square instances are equal based on their areas.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if two square instances are not equal based on their areas.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare if one square instance's area is greater than the other's.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if one square instance's area is greater
        than or equal to the other's.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare if one square instance's area is less than the other's.

        Args:
            other (Square): The other square instance to co102-square.pympare.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if one square instance's area is less
        than or equal to the other's.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
