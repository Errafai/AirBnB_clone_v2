#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
class City(BaseModel, base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
