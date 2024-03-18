#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

load_dotenv()


class DBStorage:
    """This class manages database storage for hbnb clone"""
    __engine = None
    __session = None
    
    def __init__(self):
        """Constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'), os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """query the current database session"""
        new_dict = {}
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        if cls:
            classes_to_query = [classes[cls]]
        else:
            classes_to_query = list(classes.values())
        for cls_attr in classes_to_query:
            all_objects = self.__session.query(cls_attr).all()
            for object in all_objects:
                key = object.__class__.__name__ + "." + object.id
                new_dict[key] = object
        return new_dict
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes to database"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)
                    
    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(SessionFactory)
        self.__session = Session()