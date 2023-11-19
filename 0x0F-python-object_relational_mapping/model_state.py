#!/usr/bin/python3
"""
This module contains the definition of the `State` class
using the declarative base as the Base class inherited from
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """
    The State class model using declarative base as its super class.
    (BASE): Makes state class to behave like a table, and instance of
    it as rows

    """
    __tablename__ = "states"  # Link to MySQL table `states`

    id = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
