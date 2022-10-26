#!/usr/bin/python3
"""
Unittest for class Usert
"""
import unittest
from models.user import User
from datetime import datetime
import os


class TestUser(unittest.TestCase):
    
    def test_user_email(self):
        user_1 = User()
        User.email = "otalorajuand@gmail.com"
        self.assertTrue(user_1.email == "otalorajuand@gmail.com")
