#!/usr/bin/python3
'''Write a script that changes the name of a State object from the database'''


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
    obj = db_session.query(State).filter_by(id=2).first()
    obj.name = "New Mexico"
    db_session.commit()
