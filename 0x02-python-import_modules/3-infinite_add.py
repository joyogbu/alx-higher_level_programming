#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for value in range(1, len(sys.argv)):
        total += int(sys.argv[value])
    print(total)
