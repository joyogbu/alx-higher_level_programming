#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 0:
        i = chr(i).lower()
    else:
        i = chr(i)
    print("{}".format(i), end='')
