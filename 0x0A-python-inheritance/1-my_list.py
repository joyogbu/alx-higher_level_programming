#!/usr/bin/python3
"""module returns a sorted kist object
"""


class MyList(list):
    """representing the list objes0ct class
    """
    def print_sorted(self):
        """representing the sorted list function
        """
        m_l = self[:]
        m_l.sort()
        print(m_l)

