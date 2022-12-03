#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    length = len(sys.argv[1:])
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    operators = ['+', '-', '*', '/']
    for ops in operators:
        if op not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    else:
        res = div(a, b)
    print("{:d} {} {:d} = {:d}".format(a, op, b, res))
