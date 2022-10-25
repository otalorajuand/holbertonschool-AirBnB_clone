#!/usr/bin/python3
"""
Unittest for class FileStorage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBase(unittest.TestCase):

    def test_file_path(self):

        file_1 = FileStorage()
        b_1 = BaseModel()
        b_1.save()
        self.assertTrue(os.path.exists('file.json'))
