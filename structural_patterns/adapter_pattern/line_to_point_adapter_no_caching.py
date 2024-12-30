class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def draw_point(p: Point):
    print('.', end='')


class Line:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Rectangle(list):
    """Represented as a list of lines."""
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.append(Line(Point(x, y), Point(x+width, y)))
        self.append(Line(Point(x+width, y), Point(x+width, y+height)))
        self.append(Line(Point(x, y), Point(x, y+height)))
        self.append(Line(Point(x, y+height), Point(x+width, y+height)))

class LineToPointAdapter(list):
    count: int = 0
    def __init__(self, line: Line):
        self.count += 1
        print(f'{self.count}: Generating points for line [{line.start.x}, {line.start.y}] → [{line.end.x}, {line.end.y}]')
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))

def draw(rcs):
    print("\n\n--- Drawing some stuff ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)

if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    draw(rs)