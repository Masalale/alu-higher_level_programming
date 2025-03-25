#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that inherits from Base

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The City id of the class
        name (str): The City name of the class
        state_id (int): Foreign Key to states.id
    """
    __tablename__ = 'cities'

    # Auto-generated unique integer, primary key, can't be null
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # String with maximum 128 characters, can't be null
    name = Column(String(128), nullable=False)

    # Integer, foreign key to states.id, can't be null
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
