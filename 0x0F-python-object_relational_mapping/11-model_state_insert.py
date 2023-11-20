#!/usr/bin/python3
"""
 Inserts a new instance of class 'State' into the database table
 `states`
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

    # Create session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the object to insert
    new_object = State(name='Louisiana')

    # Insert new object into table 'states'
    session.add(new_object)

    # Commit all changes made
    session.commit()

    # Query for newly inserted object id
    new = session.query(State).order_by(State.id.desc()).first()
    print(new.id)

    # Close session
    session.close()
