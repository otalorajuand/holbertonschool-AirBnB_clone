#!/usr/bin/python3
"""
Unittest for class City
"""
import unittest
from models.city import City
from datetime import datetime
import os


class TestCity(unittest.TestCase):
    
    def test_city_state_id(self):

        city_1 = City()
        self.assertTrue(hasattr(city_1, 'state_id'))
        self.assertEqual(city_1.state_id, "")
        city_1.state_id = "0500"
        self.assertEqual(city_1.state_id, "0500")


    def test_city_name(self):

        city_1 = City()
        self.assertTrue(hasattr(city_1, 'name'))
        self.assertEqual(city_1.name, "")
        city_1.name = "medellin"
        self.assertEqual(city_1.name, "medellin")
