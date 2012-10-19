# -*- coding: utf-8 -*-
import sys, unittest
class UnknownOperationError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(u"Unknown calculation operation: %s" % self.value)


def calculator(a, b, operation='+'):
    """
    This simple function executes basic math operations.
    + : adds b to a
    - : subtracts b from a
    * : multiplies b with a
    / : divides a to b
    
    rather than +,-,*,/ function raises custom error: UnknownOperationError
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return float(a) / float(b)
    else:
        raise UnknownOperationError(operation)

MY_LIB_VERSION = 1
class TestCalculator(unittest.TestCase):
    """docstring for TestCalculator"""

    def setUp(self):
        self.a = 8
        self.b = 2
    
    @unittest.skip("Just using skip") # sebeb belirtmek gerek!
    def test_addition(self):
        self.assertEqual(10, calculator(self.a, self.b))
        self.assertEqual(10, calculator(self.a, self.b, '+'))

    @unittest.skipIf(MY_LIB_VERSION >= 1, "not supported number")
    def test_subtraction(self):
        self.assertEqual(6, calculator(self.a, self.b, '-'))

    def test_multiplication(self):
        self.assertEqual(16, calculator(self.a, self.b, '*'))

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_division(self):
        self.assertEqual(4.0, calculator(self.a, self.b, '/'))

    def test_unknown_operation(self):
        self.assertRaises(UnknownOperationError,
            calculator, self.a, self.b, 'x')

    def test_addition_with_strings(self):
        self.assertEqual('ab', calculator('a', 'b'))
    
    def test_subtraction_strings(self):
        self.assertRaises(TypeError, calculator, 'a', 'b', '-')
    
    @unittest.expectedFailure
    def test_let_it_fail(self):
        self.assertEqual(1, 2)
        

if __name__ == '__main__':
    unittest.main()
