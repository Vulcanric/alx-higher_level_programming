#!/usr/bin/python3
"""Test suites for class: 'Base'
located in the module: 'models.base'
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        print('-> set up')
        self.b = Base()

    def test_id1(self):
        self.assertEqual(self.b.id, 1)

    def test_id2(self):
        self.assertEqual(self.b.id, 2)

    def test_id3(self):
        self.assertEqual(self.b.id, 3)

    def test_id52(self):
        self.b = Base(52)
        self.assertEqual(self.b.id, 52)

    def test_to_dictionary(self):
        s = Square(10, 2, 1)
        s_dictionary = s.to_dictionary()
        self.assertEqual(s_dictionary, {'id': 9, 'x': 2, 'size': 10, 'y': 1})

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, \
{'x': 2, 'width': 10, 'id': 11, 'height': 7, 'y': 8})
        self.assertEqual(json_dictionary, \
'[{"x": 2, "y": 8, "id": 11, "height": 7, "width": 10}]')

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), \
'[{"x": 2, "y": 8, "id": 6, "height": 7, "width": 10}, \
{"x": 0, "y": 0, "id": 7, "height": 4, "width": 2}]')

    def tearDown(self):
        print('-> tear down')
        del self.b
