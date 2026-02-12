import math

class Point:
    def __init__(self, x = 0, y = 0):
        if isinstance(x, (int, float)):
            self.x = x
            self.y = y
        elif isinstance(x, (list, tuple, range, Point)):
            self.x = x[0]
            self.y = x[1]
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
    def __add__(self, pt):
        return Point(self.x + pt.x, self.y + pt.y)
    def __neg__(self):
        return Point(-self.x, -self.y)
    def __sub__(self, pt):
        return self + (-pt)
    def __eq__(self, pt):
        return (self.x == pt.x) and (self.y == pt.y)
    def __neq__(self, pt):
        return not self == pt
    def __lt__(self, pt):
        return (self.x < pt.x) and (self.y < pt.y)
    def __le__(self, pt):
        return (self.x <= pt.x) and (self.y <= pt.y)
    def __gt__(self, pt):
        return (self.x > pt.x) and (self.y > pt.y)
    def __ge__(self, pt):
        return (self.x >= pt.x) and (self.y >= pt.y)
    def distance(self, pt):
        return ((self.x - pt.x)**2 + (self.y - pt.y)**2)**0.5
    def rotated(self, centre = (0, 0), angle = 0):
        t = self - Point(centre)
        r = Point(math.cos(angle)*t.x - math.sin(angle)*t.y,
                  math.sin(angle)*t.x + math.cos(angle)*t.y)
        return r + Point(centre)

class Circle:
    def __init__(self, centre = Point(0, 0), radius = 1):
        self.centre = Point(centre)
        self.radius = radius
    def __repr__(self):
        return f'Circle(centre = {self.centre}, radius = {self.radius})'
    def __str__(self):
        return f'Circle:\tCentre: {self.centre}\n        Radius: {self.radius}'
    def circumference(self):
        return 2*math.pi*self.radius
    def area(self):
        return math.pi*(self.radius)**2
    def includes(self, pt):
        return self.centre.distance(pt) <= self.radius
    def intersects(self, circ):
        return self.centre.distance(circ.centre) <= self.radius + circ.radius