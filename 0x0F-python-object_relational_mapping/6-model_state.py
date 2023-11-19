#!/usr/bin/python3
"""Link class to table in database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from urllib.parse import quote

from sqlalchemy import create_engine


username = sys.argv[1]
password = quote(sys.argv[2])
databasename = sys.argv[3]

if __name__ == "__main__":
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{databasename}',
            pool_pre_ping=True, echo=True
            )
    Base.metadata.create_all(engine)
