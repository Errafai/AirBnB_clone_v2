#!/usr/bin/python3
"""new database engine class"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """the DBStorage class"""

    __engine = None 
    __session = None
    
    def __init__(self):

        self.__engine = create_engine("mysql+mysqldb://{}.{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")
        ), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query all the objects depending on the cls, so if it is none
        we query all types of class"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)

            query = self.__session.query(cls)
            for i in query:
                key = "{}.{}".format(type(i).__name__, i.id)
                dic[key] = i

        else:
            lista = [State, City, User, Place, Review, Amenity]
            for obj in lista:
                query = self.__session.query(obj)
                for j in query:
                    key = "{}.{}".format(type(j).__name__, j.id)
                    dic[key] = j
        return dic
    
    def new(self, obj):
        """add the obj to the current session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current databse"""
        self.__session.commit()

    def delete(self, obj=None):
        """delet obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration"""
        base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()

