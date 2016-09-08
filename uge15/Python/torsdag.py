#-*- coding: utf-8 -*-
import numpy as np
from collections import Counter
import collections
import re
from re import split
import matplotlib.pyplot as plt 
import pylab as pl

N = {1: 12, 2: 15, 3: 8, 4: 4, 5: 1}
plt.bar(N.keys(), N.values(), align='center')
plt.show()

d = {'CLOVER':4,'SPADE':6,'DIAMOND':7,'HEART':2}
X = np.arange(len(d))
pl.bar(X, d.values(), align='center', width=0.5)
pl.xticks(X, d.keys())
ymax = max(d.values()) + 1
pl.ylim(0, ymax)
pl.show()


text = open('ugeseddel_data.txt', 'r').read()
words = re.findall('\w+', open('ugeseddel_data.txt').read().lower())
print collections.Counter(words)

def counterize(text):
	counter = Counter()
	for line in text:
		line = line.strip().lower()			
		if not line:
			continue
		counter.update(x for x in split("[^a-zA-Z']+", line)if x)
		X = np.arange(len(counter))
		pl.bar(X, counter.values(), align='center', width=0.5)
		pl.xticks(X, counter.keys()) 
		ymax = max(counter.values()) + 1
		pl.ylim(0, ymax)
		pl.show()
	return counter
M = counterize(text)
print 'Hvor mange gange et ord opstår: '+str(M)



