import numpy as np
from numpy.linalg import inv
import numpy.random as rnd
from numpy import linalg as LA


print "12to1"
np.ndarray
A = np.matrix('0 1 2 3 4 ; 5 6 7 8 9')
print "A:\n", A
print
A_1 = np.matrix('0 1 ; 2 3 ; 4 5 ; 6 7 ; 8 9')
print "A1:\n", A_1
print
print "12to2"
i = 3.5
j = 3.5
e = 3.5
h = 3.5
B = np.ndarray([i,j,e,h])
print "B:\n", B
print 
print "12to3 HELP!!"
C = np.arange(10)
print 
print
print "12to4"
A1 = np.arange(4)
B1 = np.asmatrix(A1)
C1 = A1.T * A1
D1 = B1.T * B1 
print "A1:\n", A1
print "B1:\n", B1
print "C1:\n", C1
print "D1:\n", D1
print
print "12to5"
M = np.eye(N=3, M=3, k=0)
print M
print
print "12to6"
a = np.matrix([[2, 1, 5, 1], [1, 1, -3, -1], [3, 6, -2, 1],[ 2, 2, 2, -3]])
print "matrix:\n", a
ainv = inv(a)
print "inverse:\n", ainv
print
print "12to7"
a1 = np.matrix([[2, 1, 5, 1], [1, 1, -3, -1], [3, 6, -2, 1],[ 2, 2, 2, -3]])
a_1 = np.random.random_sample() + inv(a1)
print "random inverse:\n", a_1
print 
print
print "12to8"
w, v = LA.eig(np.array([[1,-1],[1,1]]))
print w
print v

