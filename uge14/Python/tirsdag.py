#import numpy as np
import matplotlib
matplotlib.use("MacOSX")
import matplotlib.pyplot as plt
from matplotlib import animation
from pylab import figure, show, rand
from matplotlib.patches import Ellipse



Num=250
ells=[Ellipse(xy=rand(2)*10, width=rand(), height=rand(), angle=rand()*360) for i in range(Num)]

fig=figure()
ax=fig.add_subplot(111, aspect='equal')
for e in ells:
	ax.add_artist(e)
	e.set_clip_box(ax.bbox)
	e.set_alpha(rand())
	e.set_facecolor(rand(3))
	plt.title('14ti1')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

show()


plt.ion()
plt.figure()
x=[-5,-5]
for i in range(600):
	plt.clf() #delets the figure
	x=[x[0]+i*0.001, x[1]+i*0.001]
	plt.plot(x[0], x[1], '.') #draw a point
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	plt.title('Hej')
	plt.draw()
plt.ioff()


def drawfigure(i, ax, fig):
	"""Function that's called for each time-step"""
	ax.cla() #a method to delete the figure
	x = [-5,-5]
	x = [x[0]+i*0.1, x[1]+i*0.1]
	frame = ax.plot(x[0], x[1], 'xk')
	ax.set_title(str(x))
	ax.set_xlim(-5,5)
	ax.set_ylim(-5,5)
	plt.title('14ti2')
	return frame

fig=plt.figure(1)
ax=fig.add_subplot(111)
ani = animation.FuncAnimation(fig, drawfigure, frames=xrange(100), fargs=(ax, fig), interval=1)
plt.show()       



