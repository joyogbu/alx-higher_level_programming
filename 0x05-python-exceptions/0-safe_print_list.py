#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for items in range(x):
        try:
            print("{}".format(my_list[items]), end="")
            count += 1
        except (TypeError, IndexError):
            continue
    print()
    return(count)
