#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError as e:
        #res = e 
        pass
        if isinstance(e, Exception):
            return(False)
    return(True)
