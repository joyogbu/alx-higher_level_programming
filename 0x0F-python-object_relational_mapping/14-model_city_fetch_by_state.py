#!/usr/bin/python3
'''prints all City objects from the database'''


import sys
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State
from model_city impprt City
from sqlalchemy.orm import sessionmaker


args = sys.argv

if __name__ == "__main__":
    '''connect and query the database'''
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(args[1], args[2], args[3]))
    DBSession = sessionmaker(bind=engine)
    db_session = DBSession()
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
