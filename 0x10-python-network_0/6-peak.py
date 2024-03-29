#!/usr/bin/python3
""" A module that contains a function that finds a peak in a list of
unsorted integers."""


def find_peak(list_of_integers):
    """ A function that finds a peak in a list of unsorted integers."""
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    else:
        mid = n // 2
        if list_of_integers[mid] < list_of_integers[mid-1]:
            return find_peak(list_of_integers[:mid])
        elif list_of_integers[mid] < list_of_integers[mid+1]:
            return find_peak(list_of_integers[mid+1:])
        else:
            return list_of_integers[mid]
