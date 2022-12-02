#!/usr/bin/python3
#import hidden_4
if __name__ == "__main__":
    names = dir()
    #list_names = names.sort
    for i in names:
        if i[0:2] != '__':
            print(i)
