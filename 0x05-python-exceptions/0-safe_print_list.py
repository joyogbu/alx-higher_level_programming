#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    #list_cpy = []
    #try:
    count = 0
    for items in range(x):
        try:
            #list_cpy.append(items)
           # print(items, end = "")
            print("{}".format(my_list[items]), end = "")
            count += 1
            #print()
            #return(count)
            #return(sum(1 for i in list_cpy))
        except (TypeError, IndexError):
            continue
    print()
    return(count)
