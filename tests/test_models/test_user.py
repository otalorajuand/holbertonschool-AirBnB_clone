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
        User.password = "otalorajuand@gmail.com"
        self.assertTrue(user_1.password == "otalorajuand@gmail.com")
        self.assertTrue(type(User.password) is str)

    def test_user_first_name(self):
        user_1 = User()
        User.first_name = "otalorajuand@gmail.com"
        self.assertTrue(user_1.first_name == "otalorajuand@gmail.com")
        self.assertTrue(type(User.first_name) is str)

    def test_user_last_name(self):
        user_1 = User()
        User.last_name = "otalorajuand@gmail.com"
        self.assertTrue(user_1.last_name == "otalorajuand@gmail.com")
        self.assertTrue(type(User.last_name) is str)
