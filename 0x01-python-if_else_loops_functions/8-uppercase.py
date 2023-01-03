#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            num = chr(ord(i) - 32)
        else:
            num = i
        print("{}".format(num), end="")
    print("")
