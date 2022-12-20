#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    global res
    res = 0
    new_l = []
    for i in range(0, list_length):
        try:
            res = (my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except (ValueError, TypeError):
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_l.append(res)
    return(new_l)
