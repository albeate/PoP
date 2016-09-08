import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation
from pylab import figure, show, rand
from matplotlib.patches import Ellipse

class container(object):
	""" """
	def __init__(self, N=42, v_max=0.001, r=1):
		"""
		N: number of particles 
		v_max: maximum velocity og the paticles 
		r = radius of the container
		_init_position = initiates the positions of the particles 

		"""
		self.N = N 				
		self.v_max = v_max		
		self.r = r 				
		self._init_position() 	


	def _init_position(self):
		"""
		Initiates the positions of the particles.
		Input: N, r, and v_max.
		Output: postions. 
		"""
		self.position = np.zeros((2,self.N))
		self.velocity = np.zeros((2,self.N))

		thetha_pos = np.random.uniform(0,2*np.pi, self.N) # angels 
		thetha_v = np.random.uniform(0,2*np.pi, self.N) # angels 
		v = np.random.uniform(0,self.v_max, self.N) # speed
		R = np.random.uniform(0,self.r, self.N) # distance to center

		pol_cos = np.vectorize(lambda thetha, v: (v*np.cos(thetha))) 
		pol_sin = np.vectorize(lambda thetha, v: (v*np.sin(thetha)))
		self.velocity[0,:] = pol_cos(thetha_v,v)
		self.velocity[1,:] = pol_sin(thetha_v,v)
		#print 'self.velocity: ' + str(self.velocity)


		self.position[0,:] = pol_cos(thetha_pos,R)
		self.position[1,:] = pol_sin(thetha_pos,R)
		#print 'self.position: ' + str(self.position)

	def _step(self):
		"""
		Calculates the next steps of the particles.
		Input: dt (time-step), position, and velocity.
		Output: steps; movements of the particles, 
		"""
		dt = 50.0
		self.position = self.position+self.velocity*dt
		#print 'step: ' + str(step)

	def _willcollide(self):
		"""
		Calculates a possible collsion with the wall of the container.
		Input: c (centrum), position, velocity, and radius.
		Output: the particles should bounce back when they hit the wall of the container. 
		"""
		c = np.zeros((1,2))
		#u = 
		vector = np.vectorize(lambda x,y: self.position[0,:]-self.position[1,:])
		v_len = np.vectorize(lambda x,y: **2+y**2)
		if self.collide = vector(v_len(c, self._step())) > self.r:
			return self.position = np.add(self.position, self.velocity*u)



def drawfigure(i, ax, fig):
	"""Function that's called for each time-step""" 
	global M
	ax.cla() #a method to delete the figure
	frame = ax.plot(M.position[0,:],M.position[1,:], '.') 
	bin=plt.Circle((0,0),1,color='black',fill=False)
	fig.gca().add_artist(bin)
	ax.set_xlim(-1,1)
	ax.set_ylim(-1,1)
	M._step()
	return frame

def plot_func():
	fig=plt.figure(1)
	ax=fig.add_subplot(111)		
	ani = animation.FuncAnimation(fig, drawfigure, frames=xrange(100), fargs=(ax, fig), interval=1)
	plt.show() 


M = container()
M._step()
M._willcollide()
plot_func()




