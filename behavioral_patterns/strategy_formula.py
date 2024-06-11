import math, cmath
import unittest
from abc import ABC, abstractmethod


class DiscriminantStrategy(ABC):
    @abstractmethod
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        return discriminant

    def solve(self, a, b, c):
        discriminant = self.calculate_discriminant(a, b, c)
        root_discriminant = cmath.sqrt(discriminant)
        plus_term = (-b + root_discriminant) / (2 * a)
        minus_term = (-b - root_discriminant) / (2 * a)
        return plus_term, minus_term


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        return discriminant

    def solve(self, a, b, c):
        discriminant = self.calculate_discriminant(a, b, c)
        if discriminant < 0:
            return complex(float('nan'), float('nan')), complex(float('nan'), float('nan'))

        root_discriminant = math.sqrt(discriminant)
        plus_term = (-b + root_discriminant) / (2 * a)
        minus_term = (-b - root_discriminant) / (2 * a)
        return plus_term, minus_term


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        return self.strategy.solve(a, b, c)


class Evaluate(unittest.TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(results[0].real))
        self.assertTrue(math.isnan(results[1].real))
        self.assertTrue(math.isnan(results[0].imag))
        self.assertTrue(math.isnan(results[1].imag))


if __name__ == '__main__':
    unittest.main()