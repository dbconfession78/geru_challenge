"""
Module page_request - contains PageRequest class definition
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class PageRequest(Base):
    """
    PageRequest class definition
    :Base: declarative base that PageRequest is built on
    """
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    session_id = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False, default=datetime.utcnow)
    request = Column(String, nullable=False)
