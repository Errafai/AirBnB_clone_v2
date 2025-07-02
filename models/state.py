#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, base

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
class State(BaseModel, base):
    """ The city class, contains state ID and name """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
