#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if (length - 1) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(length-1))
        for item in range(1, len(sys.argv)):
            print("{}: {}".format(item, sys.argv[item]))
