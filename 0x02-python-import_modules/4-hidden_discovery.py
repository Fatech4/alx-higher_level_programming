#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lis = dir("hidden_4")
    for i in lis:
        if not (i[0] == "_" and i[1] == "_"):
            print("{}".format(i))
