#!/usr/bin/python3
"""
 This module defines the class model, `cities` that inherits
 from Base(declarative_base) which creates a table and
 connects it to that table in the database
"""
from relationship_state import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


class City(Base):
    """
    Class City:
        Takes Base(declarative_base) as a superclass

        Attributes:

        :__tablename__: the name of the table to create

        :id: represents an integer column in the table
            * unique
            * can't be null
            * is a primary key

        :name: represents a string column in the table
            * variable size of 128
            * can't be null

        :state_id: represents an integer column in the table
            * can't be null
            * is a foreign key referenced to State.id in the State model
    """
    __tablename__ = "cities"

    id = Column("id", Integer, unique=True, primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
