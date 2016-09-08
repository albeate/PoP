from math import sqrt


class Point(object):
	"""Represents a point in 2-D space. 
	Attributes: x, y"""

	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y


	def __str__(self):
		return "(" + str(self.x)+ "," + str(self.y) + ")" 


	def __sub__(self,other):
		return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

	def distance_between_points(self,b):
		return sqrt((self.x-b.x)**2+(self.y-b.y)**2)


	def __add__(self,other):
		if isinstance(other,Point):
			x = (self.x+other.x)
			y = (self.y+other.y)

		else:
			isinstance(other,tuple)
			x = (self.x+other[0])
			y = (self.y+other[1])
		return Point(x,y)

	#def addition(self,h):
	#	x = (self.x+h.x) 
	#	y = (self.y+h.y)
	#	return Point(x,y)
	def addition_2(self,h):
		if isinstance(h,Point):
			x = (self.x+h.x)
			y = (self.y+h.y)
		else:
			isinstance(h,tuple)
			x = (self.x+h[0])
			y = (self.y+h[1])
		return Point(x,y)

	def __eq__(self, t):
		if isinstance(t,Point):
			if self.y == t.y and self.x == t.x:
					return True
		if self.x == isinstance(t.x,tuple):
				if self.y == t.y and self.x == t.x:
						return True
		else:
			return False 

	def __radd__(self, other):
			x = (self.x+other[0])
			y = (self.y+other[1])
			return Point(x,y)




p = Point(3,8)+(5,6)
q = Point(4,3)
#print p.distance_between_points(q)
print p-q
#print p+q
print p.addition_2(q)
print p==q
print ([6,5])+Point(3,5)
print



