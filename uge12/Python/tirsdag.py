import numpy as np
import matplotlib.pyplot as plt
import time

to = time.clock()
print to

#P = lambda t: 0.5*np.matrix([0,-9.82])*t**2+np.matrix([100,100])*t
x = lambda t: 100*t
y = lambda t: -0.5*9.82*t**2+100*t


t = np.linspace(0,20,100)

#plt.plot(P[0,:],P[1,:])
plt.plot(x(t),y(t))
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["x(t)"])
plt.show()
