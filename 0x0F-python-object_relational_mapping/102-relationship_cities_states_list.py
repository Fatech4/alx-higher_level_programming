#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Create engine connection
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)

    # Create all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all cities
    cities = session.query(City).order_by(City.id).all()

    # Print cities
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
