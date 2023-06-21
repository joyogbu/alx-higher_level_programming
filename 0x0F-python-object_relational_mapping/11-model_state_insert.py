#!/usr/bin/python3
"""add new record to the states table"""

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
    new_state = State(name="Louisiana")
    db_session.add(new_state)
    db_session.commit()
    print("{}".format(new_state.id))
