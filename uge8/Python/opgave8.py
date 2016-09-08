import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from csvImageRead import csvImageRead
V = csvImageRead("Cameraman.csv")
y = np.array(csvImageRead("CameramanNoisy.csv"))


plt.figure()    # just showing the figure with color discrepancies
plt.imshow(V)
plt.show()

# (a)
def pixel(V):
	"""
	testing the pixel values from 0 to 255.
	input: pixel from image
	output: False or True
	"""
	for row in V:
		if len(V) != len(row):
			return False
		for pix in row:
			if not (0 <= pix <= 255):
				return False 
	return True

plt.imshow(V, cmap="Greys_r")  # picture shown in grey tone
plt.show()

# (b)
def gradient(V): 
	"""
	finding the gradient.
	input: pixels
	output: gradient of the pixels and two picture
	"""
	N = len(V)
	dVx = np.zeros((N,N))
	dVy = np.zeros((N,N))
	for i in range(N):
		for j in range(N):
			if j < (N-1):
				dVx[i][j] = V[i][j+1] - V[i][j]
			else: 
				dVx[i][j] = 0.0
			if i < (N-1):
				dVy[i][j] = V[i+1][j] - V[i][j]
			else: 
				dVy[i][j] = 0.0
	return dVx, dVy

dVx, dVy = gradient(V)

plt.imshow(dVx, cmap="Greys_r")  # picture shown with dVx
plt.show()

plt.imshow(dVy, cmap="Greys_r")  # picture shown with dVy
plt.show()

# (c)
def gradNorm(V1,V2):
	"""
	finding the norm.
	input: parameters V1 and V2
	output: the norm of V1 and V2 and one picture
	"""
	return np.sqrt(np.power(V1,2)+np.power(V2,2))

norm = gradNorm(dVx, dVy)

plt.imshow(norm, cmap="Greys_r")  # # picture shown with the norm energy
plt.show()


# (d)
def divergence(V1, V2):
	"""
	finding the divergence; the steeper parts of the function is shown as bright spots in the picture.
	input: V1 and V2
	output: the divergence and two pictures
	"""
	N = len(V)
	divV = np.zeros((N,N))
	for i in range(N):
		for j in range(N):
			if 0 < i < (N-1):
				y = V2[i][j] - V2[i-1][j]
			elif i == 0:
				y = (V2[i])[j]
			elif i == N-1:
				y = - (V2[i-1])[j]
			if 0 < j < (N-1):
				x = V1[i][j] - V1[i][j-1]
			elif j == 0:
				x = V1[i][j]
			elif j == N-1:
				x = - V1[i][j-1]
			divV[i][j] = y + x
	return divV

divV = divergence(dVx, dVy)

plt.imshow(divV, cmap="Greys_r")   # picture shown with divergence energy
plt.show()


# (e)
# (1)
plt.imshow(y, cmap="Greys_r")
plt.show()

# (2)
tau = 0.248
lam = 0.10

def denoise(y):
	"""
	removing noise from image by minimizing the energy; it takes some time to calculate. 
	input: pixels with noise
	output: pixels withOUT noise
	"""
	# (3)
	N = len(y)
	w1 = np.zeros((N,N))
	w2 = np.zeros((N,N))
	divW = divergence(w1, w2)

	# (4)
	ylambda = y*lam 
	ylx, yly = gradient(ylambda)

	# (5)
	f = [0 for i in range(200)]
	for k in range(200):

		# (5.1)
		divWx, divWy = gradient(-divW)
		dWx = ylx + divWx
		dWy = yly + divWy

		# (5.2)
		dWnorm = gradNorm(dWx, dWy)

		# (5.3)
		w1 = (w1-tau*dWx)/(1+dWnorm*tau)
		w2 = (w2-tau*dWy)/(1+dWnorm*tau)

		# (5.4)
		divW = divergence(w1, w2)

		# (f)
		f[k] = 0.5*np.sum(np.sum(np.power(ylambda-divW,2)))
	noise = y-(1/lam)*divW
	return noise, f

noise, f = denoise(y)

# picture without noise
plt.imshow(noise, cmap="Greys_r")   
plt.show()

# plotting, in blue, the points
plt.figure()
plt.plot(f, 'b.')
plt.show()

