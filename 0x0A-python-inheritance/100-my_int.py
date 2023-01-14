#!/usr/bin/python3
"""inverting boolean"""


class MyInt(int):
    """representing the class"""
    #def rebel(self):
        #if True:
            #return False
        #else:
            #return True
        #return bool
        #flag = not flag
        #issubclass(self, int)
    def ___eq__(self, value):
        return (int(self) != value)
    def __ne__(self, value):
        return (int(self) == value)

