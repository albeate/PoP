# -*- coding: utf-8 -*-

# Due the 28th of November 2014, by 3pm 
# Coder: Albeate (Y) :3
#
from itertools import *

class simplematrix(object):
	"""A matrix.
	Attributes: n x m and values """


	def __init__(self, m=0, n=0, values=0): # m = rows, n = colums, values = list of input
		"""
		Initiating an empty matrix. 
		"""
		self.rows = m
		self.cols = n
		self.values = values

		self.listRows = [values[i*n:(i+1)*n] for i in range(m)] #attempting to make a list comprehension
		#listRows = []
		#for i in range(m):
		#	listRows.append(values[i*n:(i+1)*n])
		#self.listRows = listRows

		self.listCols = [values[j::n] for j in range(m)] # ditto; ^as above
		#listCols = []
		#for j in range(m):
		#	listCols.append(values[j::n])
		#self.listCols = listCols

	def __str__(self):
		"""
		Prints out a matrix.
		"""
		s = ''
		for i in range(self.rows): #checking the lenght of the row
			s += '['
			for j in range(self.cols): #checking the lenght of the colum
				s +=  str(self.values[i*self.cols+j]) + ',' 
			s = s[0:(len(s)-1)]+']\n'
		return s [:-1]
	

	def read(self,filename):
		"""
		Reads to the file
		"""
		values = []
		m = 0 
		n = 0
		try:	
			with open(filename, "r") as f:
				for line in f:
					l = line[1:-2].split(',')
					m += 1
					n = len(l)
					values.extend(l)

		except IOError as e:
			print ("Ups! Reading didn't work")
		
		values = map(float, values)
		self.__init__(m,n,values)	


	def write(self,filename):
		"""
		Writes to the file
		"""
		try:	
			with open(filename, "w") as f:
				f.write(str(self))

		except IOError as e:
			print ("Ups! Writing didn't work")



	def __add__(self,other):
		"""
		Adding two matrices.
		Attributes: m x n and values
		"""
		new_matrix = []
		if self.rows == other.rows and self.cols == other.cols: #checking the size of the matrices
			new_matrix = map((lambda x,y: x + y), self.values, other.values) #adding the matrices
			return simplematrix(self.rows,self.cols,new_matrix) #returns a new matrix; new values
		else:
			raise ValueError("Ups! Can't add togehter")


	def __mul__(self,other):
		"""
		Multiplying two matrices.
		Attributes: m x n and values
		"""
		# [a,b][e,f]   [a*e+a*f,c*g+c*h] 
		# [c,d][g,h] = [b*e+b*f,d*g+d*h] 
		new_matrix = []
		if not self.cols == other.rows:
			raise ValueError ("Ups! Can't multiply togehter")
		for i in range(self.rows):
			for j in range(other.cols):
				new_matrix.append(dot(self.listRows[i],other.listCols[j]))
		return simplematrix(self.rows,other.cols,new_matrix)


	def __eq__(self,other):
		"""
		Compares the dimensions of two matrices 
		and returns True if all the elemtens are identical,
		otherwise returns False.
		Attributes: m x n and values
		"""
		if self.rows == other.rows and self.cols == other.cols:
			for i in range(len(self.values)):
				if self.values[i] != other.values[i]:
					return False
				else:
					return True
		else:
			raise ValueError ("Not of same dimensions &/or same element(s)")

	def __ne__(self, other):
		"""
		Compares the dimensions of two matrices 
		and returns False if all the elemtens are identical, 
		otherwise returns True.
		Attributes: m x n and values
		"""
		if self.rows == other.rows and self.cols == other.cols:
			for i in range(len(self.values)):
				if self.values[i] != other.values[i]:
					return True
				else:
					return False
		else:
			raise ValueError ("Not of same dimensions &/or same element(s)")


def dot(a,b):
	return sum(i*j for i,j in zip(a,b)) #Mossa's doing...




print "Now testing the simplematrix" 
A = simplematrix(2, 2, [1,2,3,4])
B = simplematrix(2, 2, [5,6,7,8])
C = simplematrix(2, 2, [6,8,10,12])
print "C == A + B: \n", C == A + B 
print "C + B: \n", C + B
print "A + B: \n", A + B
print "C == A: \n", C == A 
print "A * B: \n", A * B
print "B == A: \n", B == A 
print "A == A: \n", A == A
A.write("filname.txt")
B.write("filname.txt")
C.write("filname.txt")
A.read("filename.txt")
B.read("filename.txt")
C.read("filename.txt")


