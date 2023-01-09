#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    num_ta1 = 0
    num_ta2 = 0
    num_tb1 = 0
    num_tb2 = 0
    length1 = len(tuple_a)
    length2 = len(tuple_b)

    if length1 == 0:
        num_ta1 = 0
        num_ta2 = 0
    elif length1 == 1:
        num_ta1 = tuple_a[0]
        num_ta2 = 0
    else:
        num_ta1 = tuple_a[0]
        num_ta2 = tuple_a[1]
    if length2 == 0:
        num_tb1 = 0
        num_tb2 = 0
    elif length2 == 1:
        num_tb1 = tuple_b[0]
        num_tb2 = 0
    else:
        num_tb1 = tuple_b[0]
        num_tb2 = tuple_b[1]

    return (num_ta1 + num_tb1, num_ta2 + num_tb2)
