#!/usr/bin/python3
"""Relation with City Module"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class that inherits from Base"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement='auto'
    )
    name = Column(
        String(128),
        nullable=False
        )

    cities = relationship('City', backref=backref('state'))
