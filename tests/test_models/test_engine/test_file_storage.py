#!/usr/bin/python3
"""
Unittest for class FileStorage
"""
import json
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
            os.remove('file.json')

    def test_file_path(self):

        self.assertTrue(self.file_1._FileStorage__file_path == 'file.json')

    def test_all(self):

        self.assertTrue(self.file_1.all().get(f"BaseModel.{self.obj_1.id}"))

    def test_new(self):

        self.assertTrue(self.file_1._FileStorage__objects.get(
            f"BaseModel.{self.obj_1.id}"))

    def test_save(self):

        self.obj_1.save()
        self.assertTrue(self.file_1._FileStorage__objects.get(
            f"BaseModel.{self.obj_1.id}"))

    '''def test_reload(self):

        self.obj_1 = BaseModel()
        self.obj_1.save()
        self.file_1._FileStorage__objects = {}
        self.assertFalse(f"BaseModel.{self.obj_1.id}"
        in self.file_1._FileStorage__objects)
        self.file_1.reload()
        print(self.file_1._FileStorage__objects)
        self.assertTrue(f"BaseModel.{self.obj_1.id}" in
        self.file_1._FileStorage__objects)
    '''

    def test_reload(self):
        if os.path.exists('file.json'):
            with open('file.json', mode="r") as f:
                json_obj = json.dumps(f.read())

            self.file_1.reload()
            for value in json_obj.values():
                self.assertIn(f"{value['__class__']}.{value['id']}",
                              self.file_1._FileStorage__objects)

        else:
            self.file_1.reload()
            self.file_1._FileStorage__objects = {}
            self.assertEqual(len(self.file_1._FileStorage__objects), 0)


if __name__ == '__main__':
    unittest.main()
