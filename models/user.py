#!/usr/bin/python3
"""
User module
Defines the User class which inherits from BaseModel.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """Defines attributes for User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
