from math import *

from math import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return "Titik (" + str(self.x) + ", " + str(self.y) + ")"

    