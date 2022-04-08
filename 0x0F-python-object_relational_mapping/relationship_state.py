#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship


Base = declarative_base()


class State(Base):
    """ State class for mysql"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State")
