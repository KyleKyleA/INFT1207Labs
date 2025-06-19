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

from Lab3_Mathuran_Kyle.app.Lab3_Mathuran_Kyle import trapezium_area, rhombus_area


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

    def test_trapezium_area_ValidInputs(self):
        self.assertEqual(trapezium_area(4, 6, 6), 25)
        self.assertEqual(trapezium_area(1,1, 1 ), 1)
        self.assertEqual(trapezium_area(10, 20, 5), 75)

    def test_trapezium__area_TypeError(self):
        self.assertRaises(TypeError, trapezium_area, "five", 6, 5)
        self.assertRaises(TypeError, trapezium_area, -2, -6, -3)
        self.assertRaises(TypeError, trapezium_area, False)

    def test_trapezium_area_ValueError (self):
        self.assertRaises(ValueError, trapezium_area, 0, 0, 0 )
        self.assertRaises(ValueError, trapezium_area, -3, -7, -2)
        self.assertRaises(ValueError, trapezium_area, -5, -5)

        self.assertRaises(ValueError, trapezium_area, -5.5, 10.2, 4.1)
        self.assertRaises(ValueError, trapezium_area, -6.7, -9.3, -12.2)
        self.assertRaises(ValueError, trapezium_area, 15.5, -9.6, -2.5)

    def test_rhombus_area_TypeError(self):
        self.assertRaises(TypeError, rhombus_area, "10", 5 )
        self.assertRaises(TypeError, rhombus_area, "a","b")
        self.assertRaises(TypeError, rhombus_area, None, 5)
        self.assertRaises(TypeError, rhombus_area, [4, 5], 3)

    def test_rhombus_area_ValidInputs(self):
        self.assertRaises(rhombus_area(10, 8), 40)
        self.assertRaises(rhombus_area(2, 4), 4)
        self.assertRaises(rhombus_area(5.5, 3.2), 8.8)
        self.assertEqual(rhombus_area(7, 2.5), 8.75)



if __name__ == "__main__":
    unittest.main()
    exit()