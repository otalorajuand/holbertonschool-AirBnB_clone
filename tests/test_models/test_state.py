#!/usr/bin/python3
"""
Unittest for class State
"""
import unittest
from models.state import State
from datetime import datetime
import os


class TestState(unittest.TestCase):
    
    def test_state_name(self):

        state_1 = State()
        self.assertTrue(hasattr(state_1, 'name'))
        self.assertEqual(state_1.name, "")
        state_1.name = "Antioquia"
        self.assertEqual(state_1.name, "Antioquia")
