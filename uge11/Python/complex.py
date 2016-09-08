#addition: z1 + z2 = (a+c)+(b+d)i
#subtraktion: z1 + z2 = (a-c)+(b-d)i
#kompleks konjugation: z1^* = a-bi
#multiplikation: z1 * z2 = (a*c-b*d)+(b*c+a*d)i
#division: z1/z2 = (a*c+b*d)/(c^2+d^2)+(b*c-a*d)/(c^2+d^2)i
#a_nZ^n + a_n-1Z^n-1 + ... + a_0Z^0 

import numpy as np

class KompleksPoly(object):
	"""
	Represents a complex polynomial.
	"""
	def __init__(self, a=0.0, b=0.0, c=0.0):
		self.a = a
		self.b = b
		self.c = c

	def __str__(self):
		return "["+str(self.a) + ", " + str(self.b) + ", " + str(self.c)+"]"

	def __complex__(self):
		evaluate = complex([self.a, self.b, self.c])
		np.polyval(evaluate)
		return evaluate

a = KompleksPoly(3,5)

print a






