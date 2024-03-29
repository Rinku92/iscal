import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEquals(calculator.result,4)

    def test_add_method_calculator(self):
        calculator= Calculator()
        self.assertEqual(calculator.add(2 , 2) ,4)

    def test_sub_method_calculator(self):
        calculator= Calculator()
        self.assertEqual(calculator.sub(2 , 2) ,0)
if __name__ == '__main__':
    unittest.main()
