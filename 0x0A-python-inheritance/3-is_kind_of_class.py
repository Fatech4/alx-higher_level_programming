#!/usr/bin/python3

""" A module that has a function that returns True if the object is an
instance of, or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Argument:
    obj - Object
    a_class - Class

    Return:
    True if the object is an instance of, or if the object is an instance of
    a class that inheritted from, the specified class: otherwise False
    """
    return isinstance(obj, a_class)
