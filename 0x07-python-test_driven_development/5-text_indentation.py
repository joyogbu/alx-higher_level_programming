#!/usr/bin/python3
"""print two new lines after '.', '?' and ':' in a text
"""


def text_indentation(text):
    """defining the function"""
    if not isinstance(text, str):
    #if type(text) is not str:
        raise TypeError("test must be a string")
    else:
        text2 = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
        for i in range(len(text)):
            text2 = text2.replace('\n ', '\n')
        print(text2, end='')
