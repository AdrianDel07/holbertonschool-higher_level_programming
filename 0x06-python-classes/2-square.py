#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0):
        """Class Method Private instance attribute"""
        if type(size) is int:
            if size < 0:
                """Raised when the Value is incorrect"""
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            """Raised when the Value is incorrect"""
            raise TypeError("size must be an integer")
