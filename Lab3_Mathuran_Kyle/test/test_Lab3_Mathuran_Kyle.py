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

#region TESTING CLASS
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

    # CIRCLE TEST CASES
    def test_circle_area_TypeError(self):
        """Verify circle_area raises TypeError for invalid inputs"""
        self.assertRaises(TypeError, circle_area, 2+9j)
        self.assertRaises(TypeError, circle_area, "Hello World")
        self.assertRaises(TypeError, circle_area, True)

    def test_circle_area_ValueError(self):
        """Verify circle_area raises ValueError for invalid numeric inputs"""
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, 0)

    def test_circle_area_ValidInputs(self):
        """Verify circle_area returns correct results for valid numeric inputs"""
        self.assertEqual(circle_area(3), pi*(3**2))
        self.assertEqual(circle_area(1), pi)

    # TRAPEZIUM TEST CASES
    def test_trapezium_area_TypeError(self):
        """Verify trapezium_area raises TypeError for invalid inputs"""
        self.assertRaises(TypeError, trapezium_area, "five", 6, 5)
        self.assertRaises(TypeError, trapezium_area, 4, False, 7)

    def test_trapezium_area_ValueError(self):
        """Verify trapezium_area raises ValueError for invalid inputs"""
        self.assertRaises(ValueError, trapezium_area, 0, 0, 0)
        self.assertRaises(ValueError, trapezium_area, -5.5, 10.2, 4.1)
        self.assertRaises(ValueError, trapezium_area, -6.7, -9.3, -12.2)
        self.assertRaises(ValueError, trapezium_area, 15.5, -9.6, -2.5)

    def test_trapezium_area_ValidInputs(self):
        """Verify trapezium_area returns correct results for valid numeric inputs"""
        self.assertEqual(trapezium_area(4, 6, 6), 0.5*(4+6)*6)
        self.assertEqual(trapezium_area(1, 1, 1), 1)
        self.assertEqual(trapezium_area(10, 20, 5), 0.5*(10+20)*5)

    # ELLIPSE TEST CASES
    def test_ellipse_area_TypeError(self):
        """Verify ellipse_area raises TypeError for invalid inputs"""
        self.assertRaises(TypeError, ellipse_area, 2+9j, 1)
        self.assertRaises(TypeError, ellipse_area, 1, 2+9j)

        self.assertRaises(TypeError, ellipse_area, "Hello World", 5)
        self.assertRaises(TypeError, ellipse_area, 5, "Hello World")

        self.assertRaises(TypeError, ellipse_area, True, 8)
        self.assertRaises(TypeError, ellipse_area, 9, False)

    def test_ellipse_area_ValueError(self):
        """Verify ellipse_area raises ValueError for invalid inputs"""
        self.assertRaises(ValueError, ellipse_area, -2, 9)
        self.assertRaises(ValueError, ellipse_area, 9, -2)
        self.assertRaises(ValueError, ellipse_area, 0, 9)

    def test_ellipse_area_ValidInputs(self):
        """Verify ellipse_area returns correct results for valid numeric inputs"""
        self.assertEqual(ellipse_area(3, 4), pi*3*4)
        self.assertEqual(ellipse_area(1, 1), pi)

    # RHOMBUS TEST CASES
    def test_rhombus_area_TypeError(self):
        """Verify rhombus_area raises TypeError for invalid inputs"""
        self.assertRaises(TypeError, rhombus_area, "10", 5 )
        self.assertRaises(TypeError, rhombus_area, "a","b")
        self.assertRaises(TypeError, rhombus_area, None, 5)
        self.assertRaises(TypeError, rhombus_area, [4, 5], 3)

    def test_rhombus_area_ValueError(self):
        """Verify rhombus_area raises ValueError for invalid inputs"""
        self.assertRaises(ValueError, rhombus_area, -1, 9)
        self.assertRaises(ValueError, rhombus_area, 8, 0)

    def test_rhombus_area_ValidInputs(self):
        """Verify rhombus_area returns correct results for valid numeric inputs"""
        self.assertEqual(rhombus_area(10, 8), 80)
        self.assertEqual(rhombus_area(2, 4), 8)
        self.assertEqual(rhombus_area(5.5, 3.2), 17.6)
        self.assertEqual(rhombus_area(7, 2.5), 17.5)

#endregion TESTING CLASS

#region MAIN PROGRAM
if __name__ == "__main__":
    unittest.main()
    exit()
#endregion MAIN PROGRAM