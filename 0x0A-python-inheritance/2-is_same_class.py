#!/usr/bin/python3

""" A module that has a function that returns True if the object is an
instance of the specified class: otherwise False
"""


def is_same_class(obj, a_class):
    """
    Argument:
    obj - The object
    a_class - The Class

    Return:
    True is obj is instance of a_class and False if not
    """
    return type(obj) is a_class
