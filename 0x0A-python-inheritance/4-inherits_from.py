#!/usr/bin/python3

""" A module that has a function that returns True if the object is a
instance of a class that inherited (directly or indirectly) from the
specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Argument:
    obj - Object
    a_class - Class

    Return:
    True is obj is a subclass of a_class, False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
