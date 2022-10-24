#!/usr/bin/python3
"""this module contains the class FileStorage
"""
import json
import os.path

class FileStorage:

    __file_path= "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        dict_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[dict_key] = obj
    
    def save(self):
        """serializes __objects to the JSON file"""

        aux_dict = {key: value.to_dict() for key, value in self.all().items()}


        with open(FileStorage.__file_path, mode ="w+", encoding="utf-8") as f:
            f.write(json.dumps(aux_dict))
    
    def reload(self):
        """deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists
         ; otherwise, do nothing"""
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                str_read = f.read()
            
            python_obj = json.loads(str_read)
            return {k: eval(f"{v['__class__']}({v})") for k, v in python_obj}
        return
        
