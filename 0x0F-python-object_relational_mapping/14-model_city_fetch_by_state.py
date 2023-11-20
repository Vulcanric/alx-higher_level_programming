#!/usr/bin/python3
"""
 A program that prints all City objects from the database `hbtn_0e_14_usa`
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote


if __name__ == "__main__":
    # Get database informations

    username = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]

    # Create engine and bind it up to the session
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}',
            pool_pre_ping=True
            )

    # Create all the tables specified in the classes
    Base.metadata.create_all(bind=engine)

    # Create session inorder to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
            session.query(City, State)
            .filter(State.id == City.state_id)
            .order_by(City.id)
            )

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
