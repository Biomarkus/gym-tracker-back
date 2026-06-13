import atexit

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from typing import Callable
from sqlalchemy.orm import Session

Base = declarative_base()

engine: Engine = create_engine("sqlite:///gym.db", echo=True, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)

db_session: Callable[..., Session] = sessionmaker(autocommit=False, bind=engine)


session = db_session()



def close_session():
    if session is not None:
        session.close()

atexit.register(close_session)