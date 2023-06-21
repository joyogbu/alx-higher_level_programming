#!/usr/bin/python3
'''delete all State objects with a name containing the letter a'''


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
    all_states = db_session.query(State).filter(State.name.contains("a")).all()
    for state in all_states:
        db_session.delete(state)
    db_session.commit()
