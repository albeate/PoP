class Point(object):
	"""Represents a point in 2-D space. 
	Attributes: x, y"""


class Rectangle(object):
	"""Represent a rectangle.
	Attributes: width, height, corner"""

box = Rectangle()
box.width = 100.0
box.height = 200.0 
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rec, dx, dy):
	rec.corner.x += dx
	rec.corner.y += dy

print move_rectangle(box, 4, 5)
print box.corner.x, box.corner.y