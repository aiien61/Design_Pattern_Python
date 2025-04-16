from abc import ABC, abstractmethod


class Renderer:
    @abstractmethod
    def render_circle(self):
        raise NotImplementedError
    
class VectorRenderer(Renderer):
    def render_circle(self, radius: int):
        print(f"Drawing a circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius: int):
        print(f"Drawing pixels for a circle of radius {radius}")

class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        raise NotImplementedError
    
    @abstractmethod
    def resize(self):
        raise NotImplementedError
    
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: int):
        self.radius *= factor

if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()