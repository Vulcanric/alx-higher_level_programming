#!/usr/bin/python3
"""
 Prints the State object with the name passed as argument,
 from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote


if __name__ == "__main__":

    # Get the informations of the database to use
    username = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]

    # And the state to serach for
    st_name = sys.argv[4]

    # Create an engine to bind to the database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )

    # Create session to query database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database
    searched_state = session.query(State).filter(State.name == st_name).first()

    # Check if the state searched for, exists
    if searched_state:
        print(searched_state.id)
    else:
        print('Not found')

    # Close the session
    session.close
