#!/usr/bin/python3
for i in range(97, 123):
    c = chr(i)
    if c is not 'q' and c is not 'e':
        print("{}".format(c), end="")
