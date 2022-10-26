#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from datetime import datetime
import os


class TestUser(unittest.TestCase):
    
    def test_user_email(self):

        user_1 = User()
        self.assertTrue(hasattr(user_1, 'email'))
        self.assertEqual(User.email, "")
        user_1.email = "otalorajuand@gmail.com"
        self.assertEqual(user_1.email, "otalorajuand@gmail.com") 

    def test_user_password(self):
        
        user_1 = User()
        self.assertTrue(hasattr(user_1, 'password'))
        self.assertEqual(User.password, "")
        user_1.password = "fsdfsdf"
        self.assertEqual(user_1.password, "fsdfsdf") 


    def test_user_first_name(self):

        user_1 = User()
        self.assertTrue(hasattr(user_1, 'first_name'))
        self.assertEqual(User.first_name, "")
        user_1.first_name = "alejo"
        self.assertEqual(user_1.first_name, "alejo") 

    def test_user_last_name(self):
    
        user_1 = User()
        self.assertTrue(hasattr(user_1, 'last_name'))
        self.assertEqual(User.last_name, "")
        user_1.last_name = "garcia"
        self.assertEqual(user_1.last_name, "garcia")
