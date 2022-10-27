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
import json

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        '''
            Initializing classes
        '''
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        '''
            Cleaning up.
        '''

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        '''
            Tests the data type of the return value of the all method.
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        '''
            Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        '''
            Tests that the type of value contained in the FileStorage.__object
            is of type obj.__class__.__name__
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        '''
            Tests that a file gets created with the name file.json
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        '''
            Testing the contents of the files inside the file.json
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(type(content) is dict)

    def test_the_type_file_content(self):
        '''
            testing the type of the contents inside the file.
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reaload_without_file(self):
        '''
            Tests that nothing happens when file.json does not exists
            and reload is called
        '''

        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    ''''def test_file_path(self):

        file_1 = FileStorage()
        self.assertTrue(file_1._FileStorage__file_path == 'file.json')

    def test_all(self):

        obj_1 = BaseModel()
        file_1 = FileStorage()
        self.assertTrue(file_1.all().get(f"BaseModel.{obj_1.id}"))

    def test_new(self):

        obj_1 = BaseModel()
        file_1 = FileStorage()
        self.assertTrue(file_1._FileStorage__objects.get(f"BaseModel.{obj_1.id}"))'''



    '''def test_save(self):

        file_1 = FileStorage()
        obj_1 = BaseModel()
        obj_1.save()
        self.assertTrue(file_1._FileStorage__objects.get(f"BaseModel.{obj_1.id}"))
    '''

    
    '''
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

    
    '''def test_reload(self):

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
    '''
