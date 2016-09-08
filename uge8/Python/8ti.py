import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 8ti
def fun(X,Y):
	return X**2 + Y**2

fig = plt.figure()
ax = fig.gca(projection='3d')
plt.hold(True)
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = fun(X, Y)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)
plt.show()

#8ti1
from csvImageRead import csvImageRead
V = csvImageRead("Cameraman.csv")

def gradient(V): 
	N = len(V)
	dVx = [[0 for i in range(N)] for j in range(N)]
	dVy = [[0 for i in range(N)] for j in range(N)]
	for i in range(N):
		for j in range(N):
			if i < (N-1):
				(dVx[i])[j] = (V[i+1])[j] - (V[i])[j]
			else: 
				(dVx[i])[j] = 0.0
			if j < (N-1):
				(dVy[i])[j] = (V[i])[j+1] - (V[i])[j]
			else: 
				(dVy[i])[j] = 0.0
	return dVx, dVy

plt.figure()
plt.imshow(V)
plt.show()

plt.imshow(V, cmap="Greys_r")
plt.show()

#8ti2
def decent(x,y,z): 
	dVx, dVy = gradient(V)
	x = 0.001
	y = 0.001
	z = 50
	t >= 0
	for i in range(dVx): 
		return x - t*dVx
	for j in range(dVy):
		return y - t*dVy


fig = plt.figure()
ax = fig.gca(projection='3d')
plt.hold(True)
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, alpha=0.2)
ax.scatter(x, y, z, c='r', marker='o')
plt.show()

