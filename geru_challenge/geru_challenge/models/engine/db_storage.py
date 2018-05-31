"""
Database engine
"""

import os
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from geru_challenge.models.page_request import Base, PageRequest
from datetime import datetime


class DBStorage:
    """
    DBStorage: handles long term storage of quote requests
    """
    __engine = None
    __session = None

    def __init__(self):
        # TODO: set admin and pw in db and then here
        db = os.getenv('DB')
        self.__engine = create_engine('sqlite:///{}'.format(db))
        self.reload()
        self.request_params = {"session_id": PageRequest.session_id,
                               "request": PageRequest.request,
                               "time": PageRequest.datetime}

    def new(self, obj):
        """
        adds objects to current db session
        :param obj: object being added to db session
        :return: None
        """
        self.__session.add(obj)

    def save(self):
        """
        commits all changes of current db session
        :return: None
        """
        self.__session.commit()

    def rollback_session(self):
        """
        rollback_session - rolls back a sesssion in the event of an exception
        :return: None
        """
        self.__session.rollback()

    def get(self, params=None):
        """
        get - fetches db records
        :param params: optional dict containing db filters
        :return: list of query response dicts, 1 per record;
                 None if any param key is invalid
        """
        if params is None:
            params = {}
        lst = []
        filters = []

        for k, v in params.items():
            _filter = self.request_params.get(k)
            if not _filter:
                return ["{} is not a valid parameter".format(k)]
            filters.append(_filter == v)

        if filters:
            q = self.__session.query(
                PageRequest).filter(and_(f for f in filters))
        else:
            q = self.__session.query(PageRequest).all()

        for entry in q:
            time = datetime.strftime(entry.datetime, "%Y-%m-%d %H:%M:%S.%f")
            request = entry.request
            lst.append({
                "session_id": entry.session_id,
                "time": time,
                "request": request})

        return lst

    def delete(self, obj=None):
        """
        deletes obj from current db session if not None
        :param obj: obj to delete
        :return: None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        creates all tables in database and session from engine
        :return: None
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
        calls remove() on private session attribute, self.__session
        :return: None
        """
        self.__session.remove()
