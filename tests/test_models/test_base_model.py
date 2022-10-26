#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBase(unittest.TestCase):
    
    def test_save(self):

        base_1 = BaseModel()
        base_1.save()
        self.assertFalse(base_1.created_at == base_1.updated_at)

    def test_to_dict(self):

        base_1 = BaseModel()
        dict_aux = {'id': base_1.id, 'created_at': base_1.created_at.isoformat(), 
                    'updated_at': base_1.updated_at.isoformat(),
                    '__class__': base_1.__class__.__name__}
        self.assertEqual(dict_aux, base_1.to_dict())

    def test_id(self):

        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertFalse(base_1.id == base_2.id)

    def test_str(self):

        base_1 = BaseModel()
        str_aux = f"[BaseModel] ({base_1.id}) {base_1.__dict__}"
        self.assertEqual(str_aux, str(base_1))

    def test_created_at(self):

        base_1 = BaseModel()
        self.assertTrue(type(base_1.created_at) == datetime)

    def tearDown(self):

        if os.path.exists('file.json'):
            os.remove('file.json')

if __name__ == '__main__':
    unittest.main()
