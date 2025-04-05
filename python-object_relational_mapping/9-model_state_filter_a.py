#!/usr/bin/python3
"""lists all states contains letter a"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        user,
                        password,
                        name),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    ssn = sessionmaker(bind=eng)
    session = ssn()
    states = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
