class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x},{self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(10, 20)
other = Point(1, 2)
print((point + other).x)
point = Point.zero()
point.draw()
another = Point(3, 4)
another.draw()
