#!/usr/bin/python3
""" Creates the State "California" with the City "San Francisco" from the
database hbtn_0e_100_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    # Get MySQL credentials and database name as arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Set up connection to MySQL database using SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object and City object
    ca = State(name='California')
    sf = City(name='San Francisco')

    # Add City to State's list of cities
    ca.cities.append(sf)

    # Add State and City objects to session and commit changes to database
    session.add_all([ca, sf])
    session.commit()

    # Close session
    session.close()
