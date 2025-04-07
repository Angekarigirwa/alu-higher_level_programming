#!/usr/bin/python3
"""a script that changes the name of a State object from the database"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, name), pool_pre_ping=True)

    Session = sessionmaker(bind=eng)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()

    session.close()

