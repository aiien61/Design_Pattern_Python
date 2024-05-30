"""Liskov Substitution Principle:
Able to substitute a base type for a subtype
"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

# This Square class violates the Liskov Substitution Principle
class Square(Rectangle):
    def __init__(self, size: int):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

def use_it(rc: Rectangle):
    """This function takes a Rectangle object as an argument and calculates the expected area 
    of the rectangle based on the width and height of the rectangle. It then sets the height of 
    the rectangle to 10 and prints the expected area compared to the actual area of the rectangle.

    Parameter:
       rc: A Rectangle object.
    
    Return:
        None
    """
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(2)
    use_it(sq)
