#!/usr/bin/python3
""" Contains the class definition of a 'State' and an instance
    'Base = declarative_base()'
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Column


Base = declarative_base()


class State(Base):
    """Represents the class state which represents the 'states' table
       in the underlying database.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
