#!/usr/bin/python3
"""
 Lists all states in the `states` class via SQLAlchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from urllib.parse import quote


# Get MySQL database info
username = sys.argv[1]
password = quote(sys.argv[2])
databasename = sys.argv[3]

# Create connection engine
engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{databasename}',
        pool_pre_ping=True, echo=True
        )

# Create a session inorder to query the database
Session = sessionmaker()
session = Session(bind=engine)

states = session.query(State).order_by(State.id).all()

# Prints all states id along with their names
for state in states:
    print(f'{state.id}: {state.name}')
