import matplotlib.pyplot as plt 

print '13ti2'
def population(R, W, Rg, Wg, Rd, Wd, maxt):
	dR = 0
	dW = 0
	bunnies = []
	wolfs = []
	for i in range(1, maxt):
		R+=dR
		W+=dW
		bunnies.append(R)
		wolfs.append(W)
		dR = Rg*R-Rd*R*W
		dW = Wg*R*W-Wd*W
	return bunnies, wolfs
bunnies, wolfs = population(40, 15, 0.1, 0.005, 0.01, 0.1, 100)
plt.grid()
plt.plot(bunnies)
plt.xlabel('Time')
plt.ylabel('Population')
plt.plot(wolfs)
plt.show()