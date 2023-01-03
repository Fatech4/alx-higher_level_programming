#!/usr/bin/python3
def print_last_digit(number):
    signed = True
    if number < 0:
        signed = False
        number = -number
    last_digit = number % 10
    if not signed:
        last_digit = last_digit * -1
    return last_digit
