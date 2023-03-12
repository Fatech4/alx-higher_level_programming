#!/usr/bin/python3

""" A module that returns the list of available attributes and methods of
an object
"""


def lookup(obj):

    """ A function that accept an object as argument and return its
    attributes and methods
    """
    if obj is not None:
        return dir(obj)
