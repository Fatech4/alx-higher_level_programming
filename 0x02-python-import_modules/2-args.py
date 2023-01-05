#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if (length - 1) == 0:
        print("0 arguments.")
    elif (length - 1) == 1:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(length-1))
        for item in range(1, len(sys.argv)):
            print("{}: {}".format(item, sys.argv[item]))
