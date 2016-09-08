import matplotlib.pyplot as plt
import numpy as np
import time
time = time.clock()
print time

data = [.01, .14, .15, .21, .01, .11, .25, .32, .35, .37, .39, .45]
interv = [.1, .2, .3, .4, .5]

star = '*'
#13ti1
def valueIntervCount(data, interv):
	value = [0 for i in range(len(interv)-1)] # preventing getting out of bounce; index
	for j in data:
		for k in range(len(interv)-1):
			if j > interv[k] and j <= interv[k+1]: # checking how many items in data exits in a given interval 
				value[k] += 1
	plt.hist(data, interv)
	plt.xlabel('Data')
	plt.ylabel('Interval')
	plt.show()
	return value
print "function values: " + str(valueIntervCount(data, interv))
print 15*star

def valueIntervCount_2(data, interv):
	data = sorted(data)
	n = len(data)
	counts = []
	i = 0
	for ins in interv:
		count = 0
		while i < n and data[i]<ins:
			count += 1
			i += 1 
			counts.append(count)

	return counts[1:]
print "funcction values no. 2: " + str(valueIntervCount_2(data, interv))
print 15*star

print "numpy values: " + str(np.histogram(data, bins=interv))
print 15*star

#13ti2
def population(R, W, Rg, Wg, Rd, Wd, maxt):
	dR = Rg*R-Rd*R*W
	dW = Wg*R*W-Wd*W
	dR_2 = 0
	dW_2 = 0
	bunnies = []
	wolfs = []
	for i in range(1, maxt):
		R+=dR_2
		W+=dW_2
		bunnies.append(R)
		wolfs.append(W)
		dR_2 = Rg*R-Rd*R*W
		dW_2 = Wg*R*W-Wd*W
	return bunnies, wolfs
bunnies, wolfs = population(40, 15, 0.1, 0.005, 0.01, 0.1, 100)
plt.grid()
plt.plot(bunnies)
plt.xlabel('Time')
plt.ylabel('Population')
plt.plot(wolfs)
plt.show()


