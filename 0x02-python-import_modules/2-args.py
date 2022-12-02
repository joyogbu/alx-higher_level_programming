#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv[1:])
    ag = "argument"
    index = 1
    if int(length) == 0:
        ag = ag + 's' + '.'
    if int(length) > 1:
        ag = ag + "s" + ":"
    print("{:d} {}".format(length, ag))
    for arg in range(1, len(sys.argv)):
        if sys.argv[index] == sys.argv[0]:
            continue
        print("{}: {}" .format(arg, sys.argv[index]))
        index += 1
