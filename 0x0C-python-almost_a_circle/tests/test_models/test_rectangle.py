#!/usr/bin/python3
"""Test suite for class 'Rectangle' located in the 'models.rectangle' module"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def test_width_height(self):
        rect1 = Rectangle(8, 4)
        self.assertEqual(rect1.width, 8)
        self.assertEqual(rect1.height, 4)
        self.assertTrue(rect1.id == 4)

    def test_coordinate(self):
        rect2 = Rectangle(4, 4, x=2, y=3)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 3)
        self.assertTrue(rect2.id == 2)

    def test_setters(self):
        rect3 = Rectangle(width=0, height=0, x=0, y=0, id=0)
        rect3.width = 10
        rect3.height = 6
        rect3.x = 3
        rect3.y = 0
        self.assertTrue(rect3.width == 10)
        self.assertTrue(rect3.height == 6)
        self.assertTrue(rect3.x == 3)
        self.assertTrue(rect3.y == 0)

    def test_getters(self):  # Using class functions as if they were variables
        rect = Rectangle(45, 24, 3, 4)
        w_value = rect.width
        self.assertEqual(w_value, 45)

        h_value = rect.height
        self.assertEqual(h_value, 24)

        x_value = rect.x
        self.assertEqual(x_value, 3)

        y_value = rect.y
        self.assertEqual(y_value, 4)

    def test_accesing_private_attributes(self):
        rect = Rectangle(2048, 1024)
        rect.__x = 5
        self.assertRaises(AttributeError)

    def test_id(self):
        rect1 = Rectangle(8, 4, id=1)
        self.assertEqual(rect1.id, 1)

        rect52 = rect1 = Rectangle(8, 4, id=52)
        self.assertEqual(rect52.id, 52)
