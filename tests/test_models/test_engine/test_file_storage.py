#!/usr/bin/python3
"""
Unittest for class FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os
import models


class TestFileStorage(unittest.TestCase):

    '''def test_file_path(self):

        file_1 = FileStorage()
        self.assertTrue(file_1._FileStorage__file_path == 'file.json')

    def test_all(self):

        obj_1 = BaseModel()
        file_1 = FileStorage()
        self.assertTrue(file_1.all().get(f"BaseModel.{obj_1.id}"))

    def test_new(self):

        obj_1 = BaseModel()
        file_1 = FileStorage()
        self.assertTrue(file_1._FileStorage__objects.get(f"BaseModel.{obj_1.id}"))


    def test_save(self):

        obj_1 = BaseModel()
        file_1 = FileStorage()
        file_1.save()
        self.assertTrue(file_1._FileStorage__objects.get(f"BaseModel.{obj_1.id}"))

    
    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)'''

    
    def test_reload(self):

        obj_1 = BaseModel()
        file_1 = FileStorage()
        obj_1.name = "tatiana"
        obj_1.save()
        object_id = obj_1.id
        flag = 0
        objects = file_1.all()
        for key in objects.keys():
            if object_id in key:
                flag += 1
        self.assertTrue(flag == 1)
    
    
    def tearDown(self):

        if os.path.exists('file.json'):
            os.remove('./file.json') 
    
