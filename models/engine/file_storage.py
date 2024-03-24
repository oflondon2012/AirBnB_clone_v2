#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if type(cls) is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def delete(self, obj=None):
        """ delete an existing element"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, val in data.items():
                    obj_cls = val["__class__"]
                    obj = eval(obj_cls)(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def close(self):
        """calls reload()"""
        self.reload()
