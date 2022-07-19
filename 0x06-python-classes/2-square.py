#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Represents a square from task one.
    the Private instance attribute: size.
    Instantiation with optional size.
    """

    def __init__(self, size=0):
        """Initializes the data input.

        Args:
            size (int):the size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
