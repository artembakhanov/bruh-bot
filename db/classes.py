from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from bot.static import *
from config import DATABASE_URL

engine = create_engine(os.environ.get("DATABASE_URL", DATABASE_URL))
base = declarative_base()


class User(base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    join_date = Column(DateTime)
    banned = Column(Boolean)
    state = Column(Integer)

    def __init__(self, id, *, join_date=None, banned=False, state=DEFAULT_STATE) -> None:
        self.id = id
        self.join_date = join_date or datetime.now()
        self.banned = banned
        self.state = state


class Audio(base):
    __tablename__ = "audio"
    id = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    verified = Column(Boolean, default=False)

    def __init__(self, id, user_id, *, verified=False) -> None:
        self.id = id
        self.user_id = user_id
        self.verified = verified


base.metadata.create_all(engine)

Session = sessionmaker(bind=engine, expire_on_commit=False)
