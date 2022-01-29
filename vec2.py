import math

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%.2f,%.2f)" % (self.x, self.y)

    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y))

    def __int__(self):
        return Vec2(int(self.x), int(self.y))

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __div__(self, other):
        return Vec2(self.x / other, self.y / other)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        return self * (1.0 / self.magnitude())

    def rotate(self, angle):
        return Vec2(
                self.x * math.cos(angle) - self.y * math.sin(angle),
                self.x * math.sin(angle) + self.y * math.cos(angle))

    def toInt(self):
        return Vec2(int(self.x), int(self.y))



