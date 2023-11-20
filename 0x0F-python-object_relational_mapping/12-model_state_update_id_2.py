#!/usr/bin/python3
"""
 Updates State instance name in the database table, 'states'
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote  # Encodes special characaters


if __name__ == "__main__":
    # Get the information of the database to use

    username = sys.argv[1]
    password = quote(sys.argv[2])
    database = sys.argv[3]

    # Create an engine to bind to the database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )

    # Create a session inorder to query database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for object with id as 2 and update its name
    (
            session.query(State)
            .filter(State.id == 2)
            .update({State.name: "New Mexico"})
            )

    # Commit changes
    session.commit()

    # Close session
    session.close()
