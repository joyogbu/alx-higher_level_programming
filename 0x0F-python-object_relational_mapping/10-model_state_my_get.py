#!/usr/bin/python3
'''Write a script that lists all State objects from hbtn_0e_6_usa'''


import sys
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


args = sys.argv

if __name__ == "__main__":
    '''connect and query the database'''
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(args[1], args[2], args[3]))
    DBSession = sessionmaker(bind=engine)
    db_session = DBSession()
    all_states = db_session.query(State).filter_by(name=args[4]).first()
    if all_states is None:
        print ("Not found")
    else:
        print("{}".format(all_states.id))
