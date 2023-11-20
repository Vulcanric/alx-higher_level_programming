#!/usr/bin/python3
"""
 Print the first state in the `states` table via SQLAlchemy
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

    # Query for the first row ordered by id ascending order from table
    first_state = session.query(State).order_by(State.id.asc()).first()

    # Print the first state if it exists

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print('Nothing')

    session.close()
