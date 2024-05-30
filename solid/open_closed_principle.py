"""Open-Closed Principle:
Classese should be open for extension but closed for modification.
"""
from enum import Enum, auto
from typing import List, Iterable

# Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

    def __str__(self):
        return self.name.capitalize()

# Size = Enum('Size', ['SMALL', 'MEDIUM', 'LARGE'])
class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()

    def __str__(self):
        return self.name.title()

class Product:
    def __init__(self, name: str, size: Size, color: Color):
        self.name = name
        self.size = size
        self.color = color

class ProductFilter:
    def filter_by_color(self, products: List[Product], color: Color) -> Iterable[Product]:
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products: List[Product], size: Size) -> Iterable[Product]:
        for p in products:
            if p.size == size: yield p
    
    def filter_by_size_and_color(self, products: List[Product], size: Size, color: Color) -> Iterable[Product]:
        for p in products:
            if p.size == size and p.color == color:
                yield p

    def filter_by_size_or_color(self, products: List[Product], size: Size, color: Color) -> Iterable[Product]:
        for p in products:
            if p.size == size or p.color == color:
                yield p

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)
    
    def __or__(self, other):
        return OrSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec.is_satisfied(item), self.args))
    
class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return any(map(lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
    def filter(self, items: List[Product], spec: Specification) -> Iterable[Product]:
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    iphone = Product('iPhone', Size.SMALL, Color.GREEN)
    macbook = Product('MacBook', Size.LARGE, Color.RED)
    ipad = Product('iPad', Size.MEDIUM, Color.GREEN)
    applewatch = Product('Apple Watch', Size.SMALL, Color.BLUE)

    products = [iphone, macbook, ipad, applewatch]
    
    # approach without open closed principle
    print('without open closed principle'.center(50, '-'))
    pf = ProductFilter()

    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    print('Small products (old):')
    for p in pf.filter_by_size(products, Size.SMALL):
        print(f' - {p.name} is small')

    print('Small and green products (old):')
    for p in pf.filter_by_size_and_color(products, Size.SMALL, Color.GREEN):
        print(f' - {p.name} is small and green')

    print('Small or green products (old):')
    for p in pf.filter_by_size_or_color(products, Size.SMALL, Color.GREEN):
        print(f' - {p.name} is {p.color} and {p.size}')

    # approach with open closed principle
    print('with open closed principle'.center(50, '-'))
    bf = BetterFilter()

    print('Green products (new):')
    colorspec = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, colorspec):
        print(f' - {p.name} is green')

    print('Small products (new):')
    sizespec = SizeSpecification(Size.SMALL)
    for p in bf.filter(products, sizespec):
        print(f' - {p.name} is small')

    print('Small and green products (new):')
    for p in bf.filter(products, colorspec & sizespec):
        print(f' - {p.name} is small and green')

    print('Small or green products (new):')
    for p in bf.filter(products, colorspec | sizespec):
        print(f' - {p.name} is {p.color} and {p.size}')
