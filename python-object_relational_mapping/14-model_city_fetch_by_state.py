#!/usr/bin/python3
"""script that prints"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from model_city import City

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
    cities = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
