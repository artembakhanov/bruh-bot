import os
from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ["DATABASE_URL"])
base = declarative_base()


class User(base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    join_date = Column(DateTime)
    banned = Column(Boolean)

    def __init__(self, id, *, join_date=None, banned=False) -> None:
        self.id = id
        self.join_date = join_date or datetime.now()
        self.banned = banned


base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
