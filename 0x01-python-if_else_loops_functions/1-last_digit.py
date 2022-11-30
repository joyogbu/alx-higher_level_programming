#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_s = repr(number)
lg = number_s[-1]
if number < 0:
    lg = -int(lg)
if int(lg) > 5:
    print(f"Last digit of {number} is {lg} and is greater than 5")
elif int(lg) == 0:
    print(f"Last digit of {number} is {lg} and is 0")
elif int(lg) < 0:
    print(f"Last digit of {number} is {lg} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lg} and is less than 6 and not 0")
