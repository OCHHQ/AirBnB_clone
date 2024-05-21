#!/usr/bin/python3

"""
BaseModel module
Defines the BaseModel class which other classes inherit from.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel"""
        from models.engine.file_storage import storage

        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.now(self)

    def save(self):
        """Updates updated_at with current datetime"""
        from models.engine.file_storage import storage

        self.updated_at = datetime.now()
        storage.save()
        # Implement the logic to save to storage (e.g., file or database)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }

    def __str__(self):
        """Returns a string representation of the instance"""
        return (
            "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
            )
        )

# Adding a blank line at the end of the file
