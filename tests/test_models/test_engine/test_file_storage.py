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

    def test_file_path(self):

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

        file_1 = FileStorage()
        obj_1 = BaseModel()
        file_1.save()
        file_1._FileStorge__objects = {}
        file_1.reload()
        self.assertTrue(file_1._FileStorage__objects.get(f"BaseModel.{obj_1.id}")))

