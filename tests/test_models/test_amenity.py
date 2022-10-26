#!/usr/bin/python3
"""
Unittest for class Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    
    def test_amenity_name(self):

        review_1 = Amenity()
        self.assertTrue(hasattr(review_1, 'name'))
        self.assertEqual(review_1.name, "")
        review_1.name = "Casa del aire"
        self.assertEqual(review_1.name, "Casa del aire")


