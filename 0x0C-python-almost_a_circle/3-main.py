#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 4, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    print(Rectangle(5, 6).height)
    
    r = Rectangle(4, 3, 2)
    print(r.height)

    try:
        Rectangle(4, 6, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print(Rectangle(3, 5, 4, 6).height)
    

