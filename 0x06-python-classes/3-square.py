#!/usr/bin/python3
"""Define a square class."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initializing a square class.

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return (self.size * self.__size)
