#!/usr/bin/python3
"""Define a square."""
class Square:
    """Represents a square from task one.
    The Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """Initializes the data varibale.
        Args:
            size (int): The size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
