#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv[1:])
    ag = "argument"
    index = 1
    if int(l) == 0:
        ag = ag + 's' + '.'
    if int(l) > 1:
        ag = ag + "s" + ":"
    print("{:d} {}".format(l, ag))
    for arg in range(1, len(sys.argv)):
        if sys.argv[index] == sys.argv[0]:
            continue
        print("{}: {}" .format(arg, sys.argv[index]))
        index += 1
