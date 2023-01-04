#!/usr/bin/python3

def remove_char_at(str, n):
    str1 = ""
    for i in range(0, len(str)):
        if n > len(str):
            return str
        elif (str[i] != str[n] or n < 0):
            str1 = str1 + str[i]
        else:
            continue
    return str1
