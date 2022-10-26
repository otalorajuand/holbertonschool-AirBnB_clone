#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    
    def test_review_place_id(self):

        review_1 = Review()
        self.assertTrue(hasattr(review_1, 'place_id'))
        self.assertEqual(review_1.place_id, "")
        review_1.place_id = "Excelent"
        self.assertEqual(review_1.place_id, "Excelent")


    def test_review_user_id(self):

        review_1 = Review()
        self.assertTrue(hasattr(review_1, 'user_id'))
        self.assertEqual(review_1.user_id, "")
        review_1.user_id = "0500"
        self.assertEqual(review_1.user_id, "0500")


    def test_review_text(self):

        review_1 = Review()
        self.assertTrue(hasattr(review_1, 'text'))
        self.assertEqual(review_1.text, "")
        review_1.text = "ABCDE"
        self.assertEqual(review_1.text, "ABCDE")
