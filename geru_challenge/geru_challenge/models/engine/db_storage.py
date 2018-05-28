"""
Database engine
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ...views.page_request import Base, PageRequest



class DBStorage:
    """
    DBStorage: handles long term storage of quote requests
    """
    __engine = None
    __session = None
    def __init__(self):
        # TODO: set admin and pw in db and then here
        self.__engine = create_engine('sqlite:///geru_db.db')
        self.reload()
        

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
        rolls back a sesssion in the event of an exception
        :return:
        """
        self.__session.rollback()

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
