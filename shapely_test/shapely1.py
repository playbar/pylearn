from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon


print(Point(0,0).distance(Point(0,1)))


line = LineString([(0,0), (1,1), (1,2)])
print(line.area)
print(line.bounds)
print(line.length)
print(line.geom_type)



ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int = [(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]
polygon = Polygon(ext, [int])

print(polygon)



