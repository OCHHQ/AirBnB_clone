#!/usr/bin/python3
"""
City module
Defines the City class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """Defines attributes for City"""
    state_id = ""  # it will be the State.id
    name = ""
