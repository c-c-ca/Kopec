import unittest
from fib6 import fib6
from solution import Fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        n: int = 51
        for i, j in zip(fib6(n), Fibonacci(n)):
            self.assertEqual(i, j)


if __name__ == '__main__':
    unittest.main()