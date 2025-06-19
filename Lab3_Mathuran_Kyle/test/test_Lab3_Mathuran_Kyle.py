"""
Name: Mathuran Chandramohan, Kyle Angeles
Course: INFT 1207
Date: June 19th, 2025
Description: Set of test cases for 'calculate_area' methods along with fixtures
"""

#region IMPORTS
import unittest
from app.Lab3_Mathuran_Kyle import *

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

    def test_ellipse_area_TypeError(self):
        self.assertRaises(TypeError, ellipse_area, 2+9j, 1)
        self.assertRaises(TypeError, ellipse_area, 1, 2+9j)
        self.assertRaises(TypeError, ellipse_area, 2+9j, 3+7j)

        self.assertRaises(TypeError, ellipse_area, "Hello World", 5)
        self.assertRaises(TypeError, ellipse_area, 5, "Hello World")
        self.assertRaises(TypeError, ellipse_area, "Hello", "World")

        self.assertRaises(TypeError, ellipse_area, True, 8)
        self.assertRaises(TypeError, ellipse_area, 9, False)
        self.assertRaises(TypeError, ellipse_area, True, False)

    def test_ellipse_area_ValueError(self):
        self.assertRaises(ValueError, ellipse_area, -2, 9)
        self.assertRaises(ValueError, ellipse_area, 9, -2)
        self.assertRaises(ValueError, ellipse_area, -2, -2)

        self.assertRaises(ValueError, ellipse_area, -2.2, 9.5)
        self.assertRaises(ValueError, ellipse_area, 9.5, -2.2)
        self.assertRaises(ValueError, ellipse_area, -2.2, -9.5)

    def test_ellipse_area_ValidInputs(self):
        self.assertEqual(ellipse_area(3, 4), pi*3*4)
        self.assertEqual(ellipse_area(1, 1), pi)
        self.assertEqual(ellipse_area(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
    exit()