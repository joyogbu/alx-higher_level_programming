#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    if le == 0:
        fi = 'None'
    else:
        fi = sentence[0]
    return(le, fi)
