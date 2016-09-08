from math import sqrt
class Point(object):
	"""Represents a point in 2-D space. 
	Attributes: x, y"""


p = Point()
p.x = 3
p.y = 4

p1 = Point()
p1.x = 6
p1.y = 6


def distance_between_points(x,y):
	return sqrt((x.x-y.x)**2+(x.y-y.y)**2)

print distance_between_points(p, p1)


