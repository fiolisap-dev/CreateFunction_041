from point import *
from point3D import *

p2 = Point(30, 40)
print(p2)
print(p2.distance_from_origin())

p3 = Point(60, 80)
print("jarak 2 titik: " + str(p2.distance(p3)))

p13 = Point3D(3, 5, 8)
print(p13)