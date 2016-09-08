import copy

class Point(object):
	"""Represents a point in 2-D space. 
	Attributes: x, y"""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x)+ "," + str(self.y) + ")" 

	def __repr__(self):
		return str(self)


class Rectangle(object):
	"""Represent a rectangle.
	Attributes: width, height, corner"""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.x) + "," + str(self.y)

	def move_rectangle(self, dx, dy):
		self.x += dx
		self.y += dy

box = Rectangle()
box.width = 100.0
box.height = 200.0 
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

box.move_rectangle(5,3)
print str(box) 

#def move_rectangle(rec, dx, dy):
#	rec.corner.x += dx
#	rec.corner.y += dy
#print move_rectangle(box, 4, 5)
#print box.corner.x, box.corner.y

print 
print "deep- and shallow copy"
p = Point(3,42)
L = [p,(3,2),5]
#A = L
B = copy.copy(L)
C = copy.deepcopy(L)
p.x = 5
#print "A: ", A
print "B: ", B
print "C: ", C



