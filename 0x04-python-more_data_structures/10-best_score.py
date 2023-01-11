#!/usr/bin/python3

def best_score(a_dictionary):
    key = []
    if a_dictionary is not None:
        for i in sorted(a_dictionary):
            key.append(i)
        return key[-1]
