#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'

    # Auto-generated unique integer, primary key, can't be null
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # String with maximum 128 characters, can't be null
    name = Column(String(128), nullable=False)
