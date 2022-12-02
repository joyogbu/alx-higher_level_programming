#!/usr/bin/python3
import sys
if __name__ == "__main__":
    #values = sys.argv[1:]
    total = 0  
    #value = su(values)
    #total = int(value)
    for value in range(1, len(sys.argv)):
        #total += int(value)
        total += int(sys.argv[value])
        print(total)
