from __future__ import division
import matplotlib.pyplot as plt
from math import pi, sqrt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

kB = 1.380658*10**-23
N = 10
m = 10**-23

T = np.linspace(0,300,600)
P = lambda T: ((N*kB*T)/(pi*(2)**2))
P = np.vectorize(P)
P2 = P(T)
plt.figure()
plt.grid()
plt.plot(T, P2, color='r')
plt.xlabel('temp. measured in Kelvin')
plt.ylabel('preasure')
plt.show()

r = np.linspace(150,300,600)
P = lambda r: ((N*kB*300)/(pi*r**2))
P = np.vectorize(P)
P2 = P(r)
plt.figure()
plt.grid()
plt.plot(r, P2, color='g')
plt.xlabel('radius measured in cm^3')
plt.ylabel('preasure')
plt.show()


T = np.linspace(1,300,600)
v = lambda T: sqrt((T*kB*2)/(m))
v = np.vectorize(v)
v2 = v(T)
plt.figure()
plt.grid()
plt.plot(T, v2, color='c')
plt.xlabel('temp. measured in Kelvin')
plt.ylabel('average speed')
plt.show()



"""
GM = 2.95912208232218*10*-4 # gravitationskonstanten gange Solens masse

r_vec = np.array([-1.813068419866209*10**-1, 9.642197733507970*10**-1, -6.850809238551276*10**-5]).reshape(3,1)
v_vec = np.array([-1.718334419397708*10**-2, -3.209800047122614*10**-3, 6.736104268755766*10**-9]).reshape(3,1)


def eulerl(r_vec,v_vec, GM):
	r = np.linalg.norm(r_vec) # distance from 
	a_vec = -((GM/r**3)*r_vec)

	x = []
	y = []	
	z = []
	for i in np.arange(0,365,0.1):
		x.append(r_vec[0])
		y.append(r_vec[1])
		z.append(r_vec[2])

		r_vec += v_vec*0.5
		v_vec += a_vec*0.5

		a_vec = -((GM/r**3)*r_vec)

	coords = np.array([x,y,z])
	return coords


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xr,yr,zr = eulerl(r_vec,v_vec, GM)
ax.plot(xr, yr, zr)
plt.show()
'''
plt.figure()
plt.plot(eulerl(r_vec,v_vec,GM))
plt.show()
"""



