#!/usr/bin/python3
def safe_print_division(a, b):
    global res
    try:
        res = a / b
        return(res)
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: " "{}".format(res))
