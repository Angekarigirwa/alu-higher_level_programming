#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    s_name = sys.argv[4]
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        user,
                        password,
                        name),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    ssn = sessionmaker(bind=eng)
    session = ssn()
    s = session.query(State).filter(State.name == s_name).first()
    if s is None:
        print("Not found")
    else:
        print("{}".format(s.id))
