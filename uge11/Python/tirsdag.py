class Date(object):
	"""
	A class that represents day, month, and year.
	"""

	def __init__(self, day=0,month=0,year=0):
		"""
		Initiates a calendar.
		Attributes: day, month, and year.
		"""
		self.day = day
		self.month = month
		self.year = year
		self.monthday = [31,28,31,30,31,30,31,31,30,31,30,31]


	def __str__(self):
		"""
		Prints the date.
		Attributes: day, month, and year.
		"""
		return str(self.day+1) + "." + str(self.month+1) + "." + str(self.year+1970)


	def increment_day(self, n):
		self.day += n
		while self.day >= self.monthday[self.month]:
			self.day -= self.monthday[self.month]
			self.month += 1
			if self.day == 12:
				self.year += 1
				self.month -= 12

	def __add__(self,other):
		self.day += n
		while self.day >= self.monthday[self.month]:
			self.day -= self.monthday[self.month]
			self.month += 1
			if self.day == 12:
				self.year += 1
				self.month -= 12


date = Date()
print date
date.increment_day(377)
print date


#addition: z1 + z2 = (a+c)+(b+d)i
#subtraktion: z1 + z2 = (a-c)+(b-d)i
#kompleks konjugation: z1^* = a-bi
#multiplikation: z1 * z2 = (a*c-b*d)+(b*c+a*d)i
#division: z1/z2 = (a*c+b*d)/(c^2+d^2)+(b*c-a*d)/(c^2+d^2)i
#a_nZ^n + a_n-1Z^n-1 + ... + a_0Z^0 

class KompleksPoly(object):
	"""
	Represents a complex polynomial.
	"""
	def __init__(self, a=0.0, b=0.0):
		self.a = a
		self.b = b

	def __str__(self):
		return "["+ str(self.a) + "," + str(self.b) +"]"

	def __add__(self, other):
		return (self.a + other.a) + complex(self.b + other.b)

	def __sub__(self, other):
		return (self.a - other.a) + complex(self.b - other.b)

	def __mul__(self, other):
		return (self.a * other.a) + complex(self.b * other.b)

	def __div__(self, other):
		return ((self.a*other.a+complex(self.b*other.b))/(other.a**2+complex(other.b**2)))+((complex(self.b)*other.a-self.a*complex(other.b))/(other.a**2+complex(other.b**2)))


	def evaluate(self, z):
		add = (self.a + z.a) + complex(self.b + z.b)
		mul = (self.a * z.a) + complex(self.b * z.b)
		sub = (self.a - z.a) + complex(self.b - z.b)
		div = ((self.a*z.a+complex(self.b*z.b))/(z.a**2+complex(z.b**2)))+((complex(self.b)*z.a-self.a*complex(z.b))/(z.a**2+complex(z.b**2)))
		return add, mul, sub, div



import cmath 
#(5+6j),(13-5j)
a = KompleksPoly(5+6j)
b = KompleksPoly(4-4j)
print
print "indre:"
print a+b
print b*a
print b/a
print
print "eksterne:"
print a.evaluate(b)
print

import random
print random.randint(0,3)

def setColor(): #credit goes to Mads "med ild i haaret"
	tal = random.randint(0,3)
	if tal == 1:
		color = 'Red'
	elif tal == 2:
		color = 'Green'
	else:
		color = 'Blue'
	return color

q = setColor()
print q

liste = []

def setColor2(): #credit goes to Mdas "med ild i haaret"
	count = 0
	tal = random.randint(1,3)
	while count < 10:
		if tal == 1:
			liste.append('Red')
			color = 'Red'
			count += 1
		elif tal == 2:
			liste.append('Green')
			color = 'Green'
			count += 1
		else:
			liste.append('Blue')
			color = 'Blue'
			count += 1
			return color

p = setColor2()
print p
print liste



class glassBalls(object):
	"""
	random bowl filled with glass beads in different colors.
	"""

	def __init__(self):
		self.ost
		
	def __str__(self):
		return "you have " + str(self.ost)

	def ost(self):
		self.ost = random.randint(0,2)
		color = ["GREEN","RED","BLUE"]
		ost = color[self.ost]

		'''
		if self.ost == 1:
			ost = 'GREEN'
		elif self.ost == 2:
			ost = 'RED'
		else:
		*st = 'BLUE'
		'''
		return ost

o = glassBalls()
print o.ost()



