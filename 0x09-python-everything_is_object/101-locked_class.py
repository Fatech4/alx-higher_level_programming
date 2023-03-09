#!/usr/bin/python3
class LockedClass:
    """ A class to lock dynamically creating class attributes """
    __slots__ = ['first_name']
