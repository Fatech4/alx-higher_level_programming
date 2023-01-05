#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    sum = 0
    if length == 0:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            sum = sum + int(sys.argv[i])
        print("{}".format(sum))
