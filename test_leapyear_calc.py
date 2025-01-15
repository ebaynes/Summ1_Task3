import unittest
from leapyear_calc import leapyear_calculator

class TestLeapYear(unittest.TestCase):
    # testing years that are a leap year
    def test_is_leapyear(self):
        self.assertTrue(leapyear_calculator(2000), "The year 2000 is a leap year")
        self.assertTrue(leapyear_calculator(1988), "The year 1988 is a leap year")
    # testing years that are NOT a leap year
    def test_is_not_leapyear(self):
        self.assertFalse(leapyear_calculator(2001), "The year 2001 is not a leap year")
        self.assertFalse(leapyear_calculator(1987), "The year 1987 is not a leap year")

if __name__ == '__main__':
    unittest.main()