#!/usr/bin/python3
'''module containing the class definition of City'''


import sys
import sqlalchemy
from models_state import State, Base
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker


class City(Base):
    '''defining class for city'''
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
