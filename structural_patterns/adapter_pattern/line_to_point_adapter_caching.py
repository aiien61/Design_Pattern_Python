from typing import List, Dict

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def draw_point(p: Point) -> None:
    print('.', end='')


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

class Rectangle(list):
    """Represented as a list of lines."""

    def __init__(self, x: Point, y: Point, width: int, height: int):
        super().__init__()
        self.append(Line(Point(x, y), Point(x+width, y)))
        self.append(Line(Point(x+width, y), Point(x+width, y+height)))
        self.append(Line(Point(x, y), Point(x, y+height)))
        self.append(Line(Point(x, y+height), Point(x+width, y+height)))

class LineToPointAdapter:
    count: int = 0
    cache: Dict[int, Point] = {}

    def __init__(self, line: Line):
        self.hash = hash(line)
        if self.hash in self.cache:
            return None
        
        super().__init__()
        self.count += 1
        print(f'{self.count}: Generating points for line [{line.start.x}, {line.start.y}] → [{line.end.x}, {line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        points: List[Point] = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))
        
        self.cache[self.hash] = points

    def __iter__(self):
        return iter(self.cache[self.hash])
    
def draw(rcs):
    print('Drawing some rectangles...')
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    
    print('\n')

if __name__ == '__main__':
    rs: List[Rectangle] = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rs)
    draw(rs)
