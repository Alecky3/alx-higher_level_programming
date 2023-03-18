#!/usr/bin/python3
"""Lists all 'State' objects from the database 'hbtn_0e_6_usa'."""
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], quote_plus(sys.argv[2]),
                            sys.argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    q = session.query(State).order_by(State.id).all()
    for s in q:
        print("{}: {}".format(s.id, s.name))
