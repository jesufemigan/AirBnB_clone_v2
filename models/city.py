#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    id = Column(String(128), primary_key=True)
    state_id = Column(String(128), ForeignKey("states.id"), nullable=False)
    name = Column(String(60), nullable=False)
