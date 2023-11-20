#!/usr/bin/python3
"""
 Deletes all states in the `states` class that has the letter 'a'
 via SQLAlchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote  # Used to encode special character


if __name__ == "__main__":
    # Get MySQL database info

    username = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]

    # Create connection engine
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )

    # Create a session inorder to query the database
    Session = sessionmaker()
    session = Session(bind=engine)

    (
            session.query(State)
            .filter(State.name.like("%a%"))
            .delete()
            )
    session.commit()

    # Close the session
    session.close()
