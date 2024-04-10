#!/usr/bin/python3
"""
Module 0-add_integer.py
This module defines a function add_integer() that adds two integers.

Functions:
    add_integer(a, b=98)
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.

    The function adds two numbers, which should be integers or floats 
    (floats are converted to integers). If the numbers are not integers 
    or floats, the function raises a TypeError.

    Parameters:
    a (int, float): The first number to add. It must be an integer or float.
    b (int, float): The second number to add. It must be an integer or float. 
                    If not provided, it defaults to 98.

    Returns:
    int: The sum of a and b as an integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
