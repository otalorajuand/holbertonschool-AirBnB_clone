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

    def setUp(self):
        self.file_1 = FileStorage()
        self.obj_1 = BaseModel()

    def tearDown(self):

        if os.path.exists('file.json'):
            os.remove('./file.json') 

    def test_file_path(self):

        self.assertTrue(self.file_1._FileStorage__file_path == 'file.json')

    def test_all(self):

        self.assertTrue(self.file_1.all().get(f"BaseModel.{self.obj_1.id}"))

    def test_new(self):

        self.assertTrue(self.file_1._FileStorage__objects.get(f"BaseModel.{self.obj_1.id}"))



    def test_save(self):

        self.obj_1.save()
        self.assertTrue(self.file_1._FileStorage__objects.get(f"BaseModel.{self.obj_1.id}"))

    '''def test_reload(self):

        self.obj_1 = BaseModel()
    '''
