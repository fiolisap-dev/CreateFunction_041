from point import *

class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def translate(self, dx, dy, dz):
        Point.translate(self, dx, dy)
        self.z += dz

    def __str__(self):
        return "Titik 3D: (" + str(self.x) + \
               ", " + str(self.y) + \
               ", " + str(self.z) + ")"
    