from __future__ import division 

def denoise(y):
	N = len(y)
	w1 = [[0 for i in range(N)] for j in range(N)]
	w2 = [[0 for i in range(N)] for j in range(N)]
	divW = divergence(w1, w2)
	ylambda = [map(lambda x: x*lam, row) for row in y]
	ylx, yly = gradient(ylambda)
	for k in range(200):
		minus = [map(lambda x: -x, row) for row in divW]
		divWx, divWy = gradient(divW)
		divW = 
		dWx = [map(lambda x,y: x+y, ylx[row], divWx[row]) for row in range(N)]
		dWy = [map(lambda x,y: x+y, yly[row], divWy[row]) for row in range(N)]
		dWnorm = gradNorm(dWx, dWy)
		w1 = [map(lambda x,y,z: (x-tau*y)/(1+z*tau), w1[row], dWx[row], dWnorm[row]) for row in range(N)]
		w2 = [map(lambda x,y,z: (x-tau*y)/(1+z*tau), w2[row], dWy[row], dWnorm[row]) for row in range(N)]
		divW = divergence(w1, w2)
		noise = [map(lambda x,y: x-(1/lam)*y, y[row], divW[row]) for row in range(N)]
	return noise

noise = denoise(y)

plt.imshow(noise, cmap="Greys_r")
plt.show()