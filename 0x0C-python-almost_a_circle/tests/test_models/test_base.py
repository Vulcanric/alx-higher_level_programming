#!/usr/bin/python3
"""Test suites for class: 'Base'
located in the module: 'models.base'
"""

import unittest
from models.base import Base

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

    def tearDown(self):
        print('-> tear down')
        del self.b
