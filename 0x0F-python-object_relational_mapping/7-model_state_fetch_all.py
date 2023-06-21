#!/usr/bin/python3
'''Write a script that lists all State objects from hbtn_0e_6_usa'''


import sys
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

args = sys.argv
engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                       format(args[1], args[2], args[3]))
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

if __name__ == "__main__":
    '''connect and query the database'''
    all_states = db_session.query(State).order_by(State.id)
    for state in all_states:
        print("{}: {}".format(state.id, state.name))
