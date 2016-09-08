# 15ti2

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from collections import Counter
t = 'this is the textfile, and it is used to take words and count'

dic_freq = dict(Counter(t.split()))

dic_freq.items()

List_words = dic_freq.keys()

List_freq = dic_freq.values()


print List_words
print List_freq # printing the list with freq.

# 15ti3
# Illustrates the feq
pos = np.arange(len(List_words))
width = 0.5
height = 100


ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(List_words)

plt.bar(pos, List_freq, width, color='r')
plt.show()

#plt.hist(dic_freq.values())
#plt.title("Gaussian Histogram")
#plt.xlabel("Value")
#plt.ylabel("Frequency")
#plt.show()