#!/usr/bin/python3
"""
This module uses the sqlalchemy orm to creates a
State instance|new row in state table
and a City instance|new row in city table
and creates a relationship between the State and the City created.

Commandline Args:
    :user: The mysql username
    :password: The user password
    :database: The database to connect to
"""
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from sys import argv
from urllib.parse import quote


if __name__ == "__main__":
    # Get comandline arguments
    username = argv[1]
    password = quote(argv[2])  # parse special characters like '@'
    database = argv[3]

    # Create a connection to the database of username
    engine = create_engine(  # The engine is now my connection to the database
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
            )

    # Add all tables that has a class to the database via declarative base
    Base.metadata.create_all(engine)

    # Create a communication interface to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the intended instances
    california = State(name='California', cities=[])
    san_francisco = City(name='San Francisco', state=california)
    california.cities.append(san_francisco)

    # Add the created instances to the tables
    session.add_all([california, san_francisco])
    session.commit()
