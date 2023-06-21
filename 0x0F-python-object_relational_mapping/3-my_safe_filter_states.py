#!/usr/bin/python3
'''Displays all values in the states table of the database hbtn_0e_0_usa'''
# whose name matches that supplied as argument.


import sys
import MySQLdb


if __name__ == "__main__":
    '''define the module'''
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    # [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
    for state in c.fetchall():
        if state[1] == sys.argv[4]:
            print("{}".format(state))
