from ag_intersection import *
from a1ece650 import *
import sys
import unittest

class MyTest(unittest.TestCase):

    def test_check_input(self):
        """Test the check_command function"""
        self.assertEqual(check_command("a \"weber\" 1,2,3,4,5,6"), -1)
        self.assertEqual(check_command("a \"weber\" (1,2 (3,4) (5,6)"), -1)
        self.assertEqual(check_command("a \"weber\" (1,2)(3,4) (5,6)"), -1)
        self.assertEqual(check_command("a\"weber\" (1,2) (3,4) (5,6)"), -1)
        self.assertEqual(check_command("a \"weber\"(1,2) (3,4) (5,6)"), -1)


    def test_isupper(self):
        """Test isupper() function of class string"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('foo'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':

    unittest.main()
