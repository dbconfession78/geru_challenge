from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime


Base = declarative_base()


class PageRequest(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    session_id = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    request = Column(String, nullable=False)


#engine = create_engine('sqlite:///geru_db.db')
#Base.metadata.create_all(engine)
