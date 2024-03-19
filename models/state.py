#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # For DB
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
    # For FileStorage
    # @property
    # def cities(self):
    #     from models import storage
    #     fs_cities = storage.all(City)
    #     for city_key in fs_cities.keys():
    #         if city_key == State.id:
    #             return fs_cities[city_key]
            
