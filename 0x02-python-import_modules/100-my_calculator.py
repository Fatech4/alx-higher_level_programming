#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv) - 1
    result = 0
    if length < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if not ((op == '+' or op == '-') or (op == '*' or op == '/')):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if (op == '+'):
        result = add(a, b)
    elif (op == '-'):
        result = sub(a, b)
    elif (op == '*'):
        result = mul(a, b)
    elif (op == '/'):
        result = div(a, b)
    print("{} {} {} = {}".format(a, op, b, result))
    sys.exit(0)
