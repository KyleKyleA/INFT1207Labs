"""
Name: Mathuran Chandramohan, Kyle Angeles
Course: INFT 1207
Date: June 19th, 2025
Description: Test suite that runs test cases from 'test_area_fixtures'
"""

#region IMPORTS
import unittest
from test.test_area_fixtures import TestArea
#endregion IMPORTS

#region FUNCTIONS
def test_suite():
    # create instances of unittest
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    # add methods of TestArea to suite
    suite.addTest(TestArea('test_circle_area_TypeError'))
    suite.addTest(TestArea('test_circle_area_ValueError'))
    suite.addTest(TestArea('test_circle_area_ValidInputs'))

    print(runner.run(suite))
#endregion FUNCTIONS

#region MAIN PROGRAM
if __name__ == "__main__":
    test_suite()
    exit()
#region MAIN PROGRAM