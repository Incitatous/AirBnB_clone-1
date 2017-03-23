#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    name = ""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
