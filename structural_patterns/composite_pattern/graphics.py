from typing import List
from enum import Enum

class Color(Enum):
    RED = 'Red'
    BLUE = 'Blue'
    GREEN = 'Green'
    YELLOW = 'Yellow'

class GraphicObject:
    def __init__(self, color=None):
        self.color: Color = color
        self.children: List[GraphicObject] = []
        self._name: str = 'Group'

    @property
    def name(self):
        return self._name
    
    def _print(self, items, level: int):
        items.append('-' * level)
        if self.color:
            items.append(self.color.value)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, level+1)
        
    def __repr__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)
    
class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'
    
class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'

if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'Drawing Set'
    drawing.children.append(Square(Color.RED))
    drawing.children.append(Circle(Color.YELLOW))

    group = GraphicObject()
    group.children.append(Circle(Color.BLUE))
    group.children.append(Square(Color.BLUE))
    drawing.children.append(group)

    print(drawing)

