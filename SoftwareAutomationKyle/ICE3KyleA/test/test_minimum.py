#Region Imports
import unittest

from ICE3KyleA.app.minimum import find_minimum
#EndRegion Imports

class TestFindMinimum(unittest.TestCase):
#Region Function
    #Intializes variable "find_minimum" and reduces clutteredness to the code
    #don't have to repeat the variable in the function below
    def setUp(self):
        self.min = find_minimum()

    def tearDown(self):
        print("\n This is testing results")

    def test_all_valid(self):
        self.assertEqual(self.min.find_minimum([90]), 90)
        self.assertEqual(self.min.find_minimum([12, 10]), 10)

    def test_all_validError(self):
        self.assertRaises(ValueError, self.min.find_minimum,([23, 34.56, 67, 33]))


    def test_case3(self):
        # Min at first
        self.assertEqual(self.min.find_minimum([10, 23, 34, 81, 97]), 10)
        # Min at last
        self.assertEqual(self.min.find_minimum([97, 81, 34, 23, 10]), 10)


    def test_case4_mixed_negative(self):
        self.assertEqual(self.min.find_minimum([10, -2, 5, 23]), -2)
        self.assertEqual(self.min.find_minimum([10, -2, -24, 4]), -24)

    def test_case5_all_negatives(self):
        self.assertEqual(self.min.find_minimum([-23, -31, -45, -56]), -56)
        self.assertEqual(self.min.find_minimum([-6, -203, -2, -78]), -203)

    def test_case6(self):
        self.assertRaises(ValueError, self.min.find_minimum, ([23 ,34.56, 67, 33]))


    def test_case7_invalid_chars(self):
      self.assertRaises (ValueError, self.min.find_minimum, ([ 12, "&", "*", "34m", "!"]))

    def test_case8_repeated(self):
        self.assertEqual(self.min.find_minimum([3, 4, 6, 9, 6]), 3)
        self.assertEqual(self.min.find_minimum([13, 6, 6, 9,15]), 6)

    def test_case9_large_int(self):
        self.assertEqual(self.min.find_minimum([530, 429449672, 97, 23, 46, 59]), 23)

#EndRegion Functions
if __name__ == '__main__':
    unittest.main()
