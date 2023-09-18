#!/usr/bin/python3
"""Module containing test cases for the models.square.Square module"""
import unittest
from unittest.mock import patch
import io
import sys
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Test suite"""
    def test_Square(self):
        """Test for square object"""
        s1 = Square(5)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(s1)
            print(s1.area())
            s1.display()

            s1_display_print = mock_stdout.getvalue()
            self.assertMultiLineEqual(s1_display_print, \
"[Square] (1) 0/0 - 5\n\
25\n\
#####\n\
#####\n\
#####\n\
#####\n\
#####\n")

    def test_size_getters_setters(self):
        """Testcase for size getters and setters"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)  # testing getters

        s1.size = 10  # testing setters
        self.assertEqual(s1.size, 10)  # testing getters

        # Test for invalid size type
        with self.assertRaises(TypeError):
            s1.size = "9"  # size must be an integer

        # Test for wrong size input
        with self.assertRaises(ValueError):
            s1.size = -8  # size must be > 0

    def test_update(self):
        # Testcase for the Square method: `update`
        s1 = Square(5)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            # postional arguments
            print(s1)

            s1.update(10)
            print(s1)

            s1.update(1, 2)
            print(s1)

            s1.update(1, 2, 3, 4)
            print(s1)

            # Keyword arguments
            s1.update(x=12)
            print(s1)

            s1.update(size=7, y=1)
            print(s1)

            s1.update(size=7, id=89, y=1)
            print(s1)

            # get text printed out
            text_printed_out = mock_stdout.getvalue()
            # Compare output
            self.assertMultiLineEqual(text_printed_out, \
"[Square] (4) 0/0 - 5\n\
[Square] (10) 0/0 - 5\n\
[Square] (1) 0/0 - 2\n\
[Square] (1) 3/4 - 2\n\
[Square] (1) 12/4 - 2\n\
[Square] (1) 12/1 - 7\n\
[Square] (89) 12/1 - 7\n")
    
    def test_no_param(self):
        # test case for no parameter
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_to_dictionary(self):
        s = Square(10, 2, 1)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(s)
            s_dictionary = s.to_dictionary()
            print(s_dictionary)
            print(type(s_dictionary))

            # Get the text printed from the redirected stdout object
            text_printed = mock_stdout.getvalue()
            # Compare text printed with expected output
            self.assertMultiLineEqual(text_printed, \
"[Square] (3) 2/1 - 10\n\
{'id': 3, 'x': 2, 'size': 10, 'y': 1}\n\
<class 'dict'>\n")
