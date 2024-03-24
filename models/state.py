#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        alist = []
        ans = []
        for key in var:
            cit = key.replace('.', ' ')
            cit = shlex.split(cit)
            if (cit[0] == 'City'):
                alist.append(var[key])
        for lin in alist:
            if (lin.state_id == self.id):
                ans.append(lin)
        return (ans)
