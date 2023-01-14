#!/usr/bin/python3
"""inverting boolean"""


class MyInt(int):
    """representing the class"""
    def __eq__(self, num):
        return (int(self) != num)
    def __ne__(self, num):
        return (int(self) == num)
