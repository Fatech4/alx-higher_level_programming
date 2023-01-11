#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dictionary = {i: y for i, y in sorted(a_dictionary.items())}
    for i, j in new_dictionary.items():
        print("{}: {}".format(i, j))
