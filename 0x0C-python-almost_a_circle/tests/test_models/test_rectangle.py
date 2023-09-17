#!/usr/bin/python3
"""Test suite for class 'Rectangle' located in the 'models.rectangle' module"""
import unittest
from models.rectangle import Rectangle
import io
import sys


class TestRectangleClass(unittest.TestCase):

    def test_width_height(self):
        rect1 = Rectangle(8, 4)
        self.assertEqual(rect1.width, 8)
        self.assertEqual(rect1.height, 4)
        self.assertEqual(rect1.id, 10)

    def test_coordinate(self):
        rect2 = Rectangle(4, 4, x=2, y=3)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 3)
        self.assertTrue(rect2.id == 4)

    def test_setters(self):
        rect3 = Rectangle(width=1, height=1, x=0, y=0, id=0)
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

    def test_invalid_parameter_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "2")
            self.assertWarns("height must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.x = -10
            self.assertWarns("x must be >= 0")

        rect = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            rect.y = {}
            self.assertWarns("y must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -2
            self.assertWarns("width must be > 0")

    def test_no_parameter(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_area_method(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        rectangle = Rectangle(4, 2)

        # Store the original stdout for later resetting
        original_stdout = sys.stdout
        # create an IO object to capture printed rectangular object
        capture_object = io.StringIO()
        try:
            # Redirect stdout to the io object to capture printed text
            sys.stdout = capture_object

            # call the function to print text
            rectangle.display()
            # get the printed text
            printed_text1 = capture_object.getvalue()

            # reset width value and call again
            rectangle.width = 6
            rectangle.display()
            # get the printed text
            printed_text2 = capture_object.getvalue()

            expected_output1 = "####\n####\n"
            expected_output2 = "####\n####\n######\n######\n" #output1 included
            # Compare results
            self.assertMultiLineEqual(printed_text1, expected_output1)
            self.assertMultiLineEqual(printed_text2, expected_output2)
        finally:
            # Reset stdout back to its original state
            sys.stdout = original_stdout
