# -*- coding: utf-8 -*-
# by Beate, Freja, and Sarah
# due th 5th of december

from __future__ import division
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt


# part b)
time = time.clock()
print time


l = 250 # the wave length 
c = 1 # describes the movement of waves; only positive constants
h = 0.1 # indicates the step size between x[i]-x[i-1]
k = 0.1 # indicates the step size between t[j]-t[j-1] 

u = np.zeros((int(l/h+1),100)) # creating a grid

x = np.arange(0,l+h,h) 
t = np.linspace(0,k*100,100)

u[:,0] = np.exp(-((x-8)**2)/(4)) # boundary conditions for zero 
u[:,1] = np.exp(-((x-8-c*k)**2)/(4)) # boundary conditions for k


for j in range(1,99):
	for i in range(1,int(l/h)):
		u[i,j+1] = 2*u[i,j]-u[i,j-1] + ((u[i+1,j]-2*u[i,j]+u[i-1,j])*k**2*c**2)/(h**2)



plt.ion()
plt.figure()
plt.grid()
plt.xlabel("t")
plt.ylabel("u(t)")
plt.legend(["u"])

for i in np.arange(1,100,10):
	plt.plot(x, u[:,i])		
	plt.draw()
	plt.ioff()

