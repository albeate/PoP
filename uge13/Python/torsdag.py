from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, e
import time


time = time.clock()
print 'Time it takes the program to run:' + str(time)
print 
print "13to1"
y = [1, 2, 3, 4, 5, 6, 7,8 ,9 ,10]
x = [4.080, 3.991, 4.094, 4.107, 4.056, 3.978, 4.112, 4.174, 4.198, 3.967]

plt.figure()
plt.grid()
plt.plot(x)
plt.xlable("")

print '(a) standard deviation'
def meanVal(x):
	return (1/len(x))*sum(x)
print "function value: " + str(meanVal(x))
print
print '(b) spredning'
def stdDev(x):
	std = sqrt(sum(map(lambda xi: (xi-meanVal(x))**2, x))/(len(x)-1)) 
	return std
print "function value: " + str(stdDev(x)) # unbiased sample 
print "numpy value: " + str(np.std(x)) # biased sample
print "The reason for the deviations is due to unbiased/biased sample methods."
print


print '(c)'
#np.linspace(start, stop, num=50, endpoint=True, retstep=False)
def normalDist(x):
	dist = map(lambda xi: (1/(stdDev(x)*sqrt(2*pi)))*(e**(-((xi-meanVal(x))**2)/(2*stdDev(x)**2))), x)
	return sorted(dist) 
print "function value: " + str(normalDist(x))

plt.figure()
plt.grid()
plt.plot(normalDist(x), 'c')
plt.show()

print
print '13to2'
print '(a)'
print "numpy value: " + str(np.mean(x))
print
print '(b)'

#def medianVal(x): # nope!
#	median = len(x)/2
#	x.sort()
#	if len(x) / 2 == 0 :
#		return (x[median-1]+x[median])/2
#	else:
#		return x[median]
#print medianVal(x)

def medianVal(x):
    return (sorted(x)[int(round((len(x)-1)/2))]+sorted(x)[int(round((len(x)-1)/2))])/2
print "function values: " + str(medianVal(x))
print "numpy values: " + str(np.median(x))

