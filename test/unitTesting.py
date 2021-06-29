import unittest
import main
class testing(unittest.TestCase):
    def test_calculator(self):
        #AssertEqual eg
        self.assertEqual(main.salary_calculator(45000),45000)

        #AsserFalse eg
        self.assertFalse(main.salary_calculator(65000>50000),"not valid")

        #AssertGreater eg
        self.assertGreater(45000,50000,"---Invalid--- ")

        #asserRaises eg
        self.assertRaises(Exception,main.salary_calculator())

