#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place
from datetime import datetime
import os


class TestPlace(unittest.TestCase):
    
    def test_place_city_id(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'city_id'))
        self.assertEqual(place_1.city_id, "")
        place_1.city_id = "0500"
        self.assertEqual(place_1.city_id, "0500")

    def test_place_user_id(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'user_id'))
        self.assertEqual(place_1.user_id, "")
        place_1.user_id = "10369549"
        self.assertEqual(place_1.user_id, "10369549") 


    def test_place_name(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'name'))
        self.assertEqual(place_1.name, "")
        place_1.name = "casa en el aire"
        self.assertEqual(place_1.name, "casa en el aire") 


    def test_place_description(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'description'))
        self.assertEqual(place_1.description, "")
        place_1.description = "excelente"
        self.assertEqual(place_1.description, "excelente") 


    def test_place_number_rooms(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'number_rooms'))
        self.assertEqual(place_1.number_rooms , 0)
        place_1.number_rooms = 3
        self.assertEqual(place_1.number_rooms, 3)


    def test_place_number_bathrooms(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'number_bathrooms'))
        self.assertEqual(place_1.number_bathrooms , 0)
        place_1.number_bathrooms = 2
        self.assertEqual(place_1.number_bathrooms, 2)


    def test_place_max_guests(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'max_guest'))
        self.assertEqual(place_1.max_guest, 0)
        place_1.max_guest = 5
        self.assertEqual(place_1.max_guest, 5)

    def test_place_price_by_night(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'price_by_night'))
        self.assertEqual(place_1.price_by_night, 0)
        place_1.price_by_night = 20000
        self.assertEqual(place_1.price_by_night, 20000)


    def test_place_latitude(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'latitude'))
        self.assertEqual(place_1.latitude, float(0))
        place_1.latitude = 5.5
        self.assertEqual(place_1.latitude, 5.5)


    def test_place_longitude(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'longitude'))
        self.assertEqual(place_1.longitude, float(0))
        place_1.longitude = 5.5
        self.assertEqual(place_1.longitude, 5.5)

    def test_place_amenity_ids(self):

        place_1 = Place()
        self.assertTrue(hasattr(place_1, 'amenity_ids'))
        self.assertEqual(place_1.amenity_ids, "")
        place_1.amenity_ids = "excelent"
        self.assertEqual(place_1.amenity_ids, "excelent")
