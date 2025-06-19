"""
Name: Mathuran Chandramohan, Kyle Angeles
Course: INFT 1207
Date: June 19th, 2025
Description: Set of test cases for 'calculate_area' methods along with fixtures
"""

#region IMPORTS
import unittest
from app.calculate_area import *

from math import pi
#endregion IMPORTS

class TestArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up test class")

    def setUp(self):
        print("Setting up test")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test class")

    def tearDown(self):
        print("End of test")

    def test_circle_area_TypeError(self):
        self.assertRaises(TypeError, circle_area, 2+9j)
        self.assertRaises(TypeError, circle_area, "Hello World")
        self.assertRaises(TypeError, circle_area, True)

    def test_circle_area_ValueError(self):
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -2.2)

    def test_circle_area_ValidInputs(self):
        self.assertEqual(circle_area(3), pi*(3**2))
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)

if __name__ == "__main__":
    unittest.main()
    exit()