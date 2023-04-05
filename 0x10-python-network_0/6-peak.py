#!/usr/bin/python3
""" find a peak in an unsorted list of integers """


def find_peak(list_of_integers):
    """ define yhe function """
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
