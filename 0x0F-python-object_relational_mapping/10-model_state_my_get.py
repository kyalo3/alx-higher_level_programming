#!/usr/bin/python3
"""
a script that prints the State object
with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    """create an SQLAlchemy engine"""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    """create a Session class"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """query the database and print results"""
    state = session.query(State).order_by(State.id).first()

    for state in session.query(State):
        if argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")

    """close the session"""
    session.close()
