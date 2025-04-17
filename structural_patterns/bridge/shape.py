import abc

# Implementor
class Color(abc.ABC):
    @abc.abstractmethod
    def fill(self): pass

class Red(Color):
    def fill(self) -> str:
        return "Red"
    
class Blue(Color):
    def fill(self) -> str:
        return "Blue"
    
# Abstraction
class Shape:
    def __init__(self, color: Color):
        self.color = color
    
    def draw(self): pass

# Refined Abstraction
class Circle(Shape):
    def draw(self):
        return f"Draw a circle filled with {self.color.fill()}"
    
class Square(Shape):
    def draw(self):
        return f"Draw a square filled with {self.color.fill()}"

if __name__ == "__main__":
    red = Red()
    blue = Blue()


    circle = Circle(red)
    square = Square(blue)

    print(circle.draw())
    print(square.draw())