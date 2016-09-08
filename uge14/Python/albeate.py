from __future__ import division
import matplotlib.pyplot as plt
from matplotlib import animation
from pylab import figure, show, rand
#from matplotlib.patches import Ellipse
from math import pi, sqrt, cos, sin 
import numpy as np
import random

"""

kB = 1.380658*10**-23          # 
N = 10                         # Number of particles 
m = 10**-23                    # The mass of the particles
T = np.linspace(0,300,600)     # The temp., in Kelvin, in an interval from 0 to 300
r = np.linspace(150,300,600)   # The radius 
t = 0.5 					   # The change (delta) in time, which is constant 

v = np.arange(3, 4)            # Vectors
s = 3      					   # Scalar
p = np.linspace(0,4)						   # Position
c = 0.0 					   # Centrum 

def scale(v, s):
	"""#Returns the scalar product"""
	scalar = (v*s)/np.norm(v)
	return scalar

def proj(p, v):
	"""Projection of a point unto a vector"""
	return (np.dot(p,v)/np.norm(v))*v/np.norm(v)

def step(p, t, v):
	"""Calculates the distance and wheter or not the containers centrum is bigger than its radius"""
	return p[0]+t*v[0], p[1]+t*v[1]

def vec(p1, p2):
	""" """
	return p1[0]-p2[0], p1[1]-p2[1]

class Molecule(object):
	"""Simulates the movements of the molecules"""
	def __init__(self, p, v, r):
		self.p = p #The particles current position
		self.v = v 
		self.r = r #The container's radius 

	def willcolide(self, p, r, t):
		c = 0.0
		if np.linalg.norm(vec(c,step(p, t))) > r:
			return True 
		else:
			return False

	def newPosition(self):
		if willcolide(p, r, t) == True:
			pass


p1 = p
vp = vec(p1,proj(p1(vec(c,pc))))
p1 = np.add(p1,scale(vp,2*np.linalg.norm(vp)))
v2 = scale(vec(pc,p1),np.linalg.norm(v))


def visual(self):
		fig=plt.figure()
		ax=fig.add_subplot(1,1,1)
		circ=plt.Circle((0,0), radius=10, color='g', fill=False)
		ax.add_patch(circ)
		plt.show()
		pass
"""

thetha = np.random.uniform(0,2*pi) #Random selects an angles from an interval thetha \in [0, 2*pi]
v_lenght = np.random.uniform(0,1) #Random selects a speed from an interval v \in [0,v_max]
print (v_lenght*np.cos(thetha),v_lenght*np.sin(thetha))

print np.linalg.norm(vec(c,step(p, t)))


print 'P'
P = lambda T: ((N*kB*T)/(pi*(2)**2))
P = np.vectorize(P)
P2 = P(T)
print P
print 

print 'P2'
P = lambda r: ((N*kB*300)/(pi*r**2))
P = np.vectorize(P)
P2 = P(r)
print P2
print

print 'v2'
v = lambda T: sqrt((T*kB*2)/(m))
v = np.vectorize(v)
v2 = v(T)
print v2





"""
plt.ion()
fig = plt.figure()
ax=fig.add_subplot(1,1,1)
circ=plt.Circle((200,200), radius=10, color='g', fill=False)
ax.add_patch(circ)
x=[-5,-5]
for i in range(600):
	plt.clf() #delets the figure
	x=[x[0]+i*0.001, x[1]+i*0.001]
	plt.plot(x[0], x[1], '.') #draw a point
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	plt.draw()

plt.ioff()
"""


plt.ion()
for i in range(2):
	fig = plt.figure()
	ax = fig.add_subplot(4,4,i+1)
	circ = plt.Circle((0,0), 10, color='g', fill=False)
	ax.add_subplot(circ)
	x = [-5,-5]
	plt.clf() #delets the figure
	x=[x[0]+i*0.001, x[1]+i*0.001]
	plt.plot(x[0], x[1], '.') #draw a point
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	plt.draw()
plt.ioff()







