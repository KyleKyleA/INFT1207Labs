"""
Name: Mathuran Chandramohan, Kyle Angeles
Course: INFT 1207
Date: June 19th, 2025
Description: Test suite that runs test cases from 'test_area_fixtures'
"""

#region IMPORTS
import unittest
from test.test_Lab3_Mathuran_Kyle import TestArea
#endregion IMPORTS

#region CONSTANTS
GREETING = """Program will perform test cases for calculating area
on the following shapes:"""

MENU = ("""1. Circle
2. Trapezium
3. Ellipse
4. Rhombus""")

MENU_OPTIONS  = [1, 2, 3, 4]

PROMPT = "Choose shape: "
#endregion CONSTANTS

#region FUNCTIONS
#region unittest
def test_suite(shape: str):
    # create instances of unittest
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    if shape == 1:
        suite.addTest(TestArea('test_circle_area_TypeError'))
        suite.addTest(TestArea('test_circle_area_ValueError'))
        suite.addTest(TestArea('test_circle_area_ValidInputs'))

    elif shape == 3:
        suite.addTest(TestArea('test_ellipse_area_TypeError'))
        suite.addTest(TestArea('test_ellipse_area_ValueError'))
        suite.addTest(TestArea('test_ellipse_area_ValidInputs'))

    print(runner.run(suite))
#endregion unittest

#region helpers
def validate_int_range(prompt: str, valid_int: list [int]):
    """Prompts user for integer input and checks if it's within the specified range"""
    while True:
        try:
            # prompt user for input
            int_input = int(input(prompt))

            # checks if number is within specified range
            if int_input not in valid_int:
                raise Exception(f"Number input must be within specified range: {valid_int}!")

            return int_input
        except ValueError as v:
            print(f"{v}. Only integer values are accepted!")
            continue
        except Exception as e:
            print(e)
            continue

#endregion helpers
#endregion FUNCTIONS

#region MAIN PROGRAM
if __name__ == "__main__":
    # greet user and explain program
    print("-"*40)
    print(GREETING)
    print(MENU)
    print("-" * 40)

    # prompt user for input
    user_input = validate_int_range(PROMPT, MENU_OPTIONS)
    print("-" * 40)

    # run test cases for requested shape
    test_suite(user_input)

    exit()
#region MAIN PROGRAM