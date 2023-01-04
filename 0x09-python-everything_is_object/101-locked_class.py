#!/usr/bin/python3
"""class prevent dynamic creation of class and instance attribute"""


class LockedClass:
    """representing LockedClass class"""
    __slots__ = ['first_name']
