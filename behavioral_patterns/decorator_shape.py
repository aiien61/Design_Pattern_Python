import unittest
import logging
from abc import ABC, abstractmethod
from enum import Enum, auto

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Color(Enum):
    YELLOW = auto()
    GREEN = auto()
    RED = auto()
    BLUE = auto()
    BLACK = auto()
    WHITE = auto()
    ORANGE = auto()


class Shape(ABC):
    @abstractmethod
    def __str__(self): return 'Unknown shape'


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius: int = radius

    def resize(self, factor: float) -> bool:
        self.radius *= factor
        return True

    def __str__(self):
        return f'A circle of radius {self.radius}'
    

class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side: int = side
    
    def __str__(self):
        return f'A square wiht side {self.side}'
    

class ColoredShape(Shape):
    def __init__(self, shape: Shape, color: Color) -> None:
        if isinstance(shape, ColoredShape):
            raise Exception("Can't apply ColoredShape twice.")
        self.shape: Shape = shape
        self.color: Color = color

    def __str__(self):
        return f'{self.shape.__str__()} has color {self.color.name}'
    
    def resize(self, factor: float) -> bool:
        if isinstance(self.shape, Square):
            return False
        return self.shape.resize(factor)

class TransparentShape(Shape):
    def __init__(self, shape: Shape, alpha: float):
        self.shape: Shape = shape
        self.alpha: float = alpha
        if alpha < -1 or alpha > 1:
            raise ValueError('alpha must be less or equal to 1.')
        
    def __str__(self):
        return f'{self.shape.__str__()} has {self.alpha * 100.0}% transaparency'
    
    def resize(self, factor: float) -> bool:
        if isinstance(self.shape, Square):
            return False
        return self.shape.resize(factor)
    

class Test(unittest.TestCase):
    def test_circle(self):
        circle = Circle(2)
        expected = 'A circle of radius 2'
        self.assertEqual(expected, str(circle))

    def test_colored_circle(self):
        circle = Circle(2)
        red_circle = ColoredShape(circle, Color.RED)
        expected = 'A circle of radius 2 has color RED'
        self.assertEqual(expected, str(red_circle))

    def test_resize_in_circle(self):
        circle = Circle(2)
        circle.resize(3)
        expected = 'A circle of radius 6'
        self.assertEqual(expected, str(circle))

    def test_resize_in_colored_circle(self):
        circle = Circle(2)
        red_circle = ColoredShape(circle, Color.RED)
        red_circle.resize(3)
        expected = 'A circle of radius 6 has color RED'
        self.assertEqual(expected, str(red_circle))
    
    def test_transparent_circle(self):
        circle = Circle(2)
        half_transparent_circle = TransparentShape(circle, 0.5)
        expected = 'A circle of radius 2 has 50.0% transaparency'
        self.assertEqual(expected, str(half_transparent_circle))

    def test_transparent_colored_circle(self):
        circle = Circle(2)
        red_circle = ColoredShape(circle, Color.RED)
        red_half_transparent_circle = TransparentShape(red_circle, 0.5)
        expected = 'A circle of radius 2 has color RED has 50.0% transaparency'
        self.assertEqual(expected, str(red_half_transparent_circle))

    
    def test_square(self):
        square = Square(5)
        expected = 'A square wiht side 5'
        self.assertEqual(expected, str(square))

    def test_colored_square(self):
        square = Square(5)
        green_square = ColoredShape(square, Color.GREEN)
        expected = 'A square wiht side 5 has color GREEN'
        self.assertEqual(expected, str(green_square))
    
    def test_no_resize_in_square(self):
        try:
            square = Square(5)
            square.resize(2)
        except AttributeError as e:
            logging.debug(e)
        finally:
            expected = 'A square wiht side 5'
            self.assertEqual(expected, str(square))

    def test_no_resize_in_colored_square(self):
        square = Square(5)
        green_square = ColoredShape(square, Color.GREEN)
        self.assertFalse(green_square.resize(2))
        
        expected = 'A square wiht side 5 has color GREEN'
        self.assertEqual(expected, str(green_square))


if __name__ == '__main__':
    unittest.main()
