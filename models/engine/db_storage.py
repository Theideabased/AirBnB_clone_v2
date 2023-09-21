#!/usr/bin/python3
"""DBStorage module"""

from sqlalchemy import create_engine, MetaData
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

# Environment variables
mysql_user = os.getenv('HBNB_MYSQL_USER')
mysql_password = os.getenv('HBNB_MYSQL_PWD')
mysql_host = os.getenv('HBNB_MYSQL_HOST')
mysql_db = os.getenv('HBNB_MYSQL_DB')
hbnb_env = os.getenv('HBNB_ENV')


class DBStorage:
    """Class for db storage"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                mysql_user,
                mysql_password,
                mysql_host,
                mysql_db
            ), pool_pre_ping=True)

        if hbnb_env == 'test':
            metadata = MetaData()

            # Reflect all existing tables from database into the MetaData obj
            metadata.reflect(bind=engine)

            # Drop all the tables
            metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """Returns dictionary of database"""
        if cls is None:
            data = self.__session.query(State).all()
            data.extend(self.__session.query(City).all())
            data.extend(self.__session.query(User).all())
            data.extend(self.__session.query(Place).all())
            data.extend(self.__session.query(Review).all())
            data.extend(self.__session.query(Amenity).all())
        else:
            data = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in data}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
