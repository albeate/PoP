#
# assignment 3
#
# Finding the limit by using the "Newton Method" 
# by B! :) 



from __future__ import division
from math import sin
from math import exp
import scipy
import time



def fp(f,x,h): # help function 
	"""
		This function takes the foreward derivative. 
	input: numerical values
	output: the limit 
	"""
	return (f(x+h)-f(x))/h

def newt(f,a,b): 
	"""
		Takes the limit by using Newton's method: cn+1 = cn - f(cn)/f'(cn).
	input: any interval of the function 
	output: the limit 
	"""
	cn = a+(a-b)/2
	h = 10e-16
	cn1 = cn - f(cn)/fp(f,cn,h)
	if fp(f,cn,h) == 0:
		return "You're attempting to do something that is not okay..."
	else: 
		for i in range(10000): # n max
			
			cn1 = cn - (f(cn)/fp(f,cn,h))
			if abs(f(cn1) - f(cn)) < h: # nothing's happening anymore. 
				return cn1 
			if abs(f(cn1)) < h: # whether or not it has converged. 
				return cn1
			if abs(cn) < h:
				return 0 
			if fp(f,cn,h) == 0: # if f' equals zero. 
				return 'blah!'
			cn = cn1

			
		return cn


"""
	Ex. functions to test the program.
	lambda is used to shorten my code. 
"""
f = lambda x: x**2 - 3
g = lambda x: x*sin(1/x)
h = lambda x: exp(x) - 1


"""
	Test run of the program using the given functions above.  
"""
eps = 10e-16
delimiter = "-"
print "testing "
print newt(f,-2,2)
print newt(g,0.01,0.1)
print newt(h,-1,1)
print 
print "evaluating f(c)"
print delimiter*15
print (newt(f,-2,2))**2-3
print (newt(g,0.01,0.1))*sin(1/(newt(g,0.01,0.1)))
print exp(newt(h,-1,1))-1
print
print "evaluating f(c + eps)"
print delimiter*15
print ((newt(f,-2,2))+eps)**2-3
print ((newt(g,0.01,0.1))+eps)*sin(1/((newt(g,0.01,0.1))+eps))
print exp((newt(h,-1,1))+eps)-1
print
print "evaluating f(c - eps)"
print delimiter*15
print ((newt(f,-2,2))-eps)**2-3
print ((newt(g,0.01,0.1))-eps)*sin(1/((newt(g,0.01,0.1))-eps))
print exp((newt(h,-1,1))-eps)-1
print 
print 




def countdown(count):
    while (count >= 1):
        print ('Better start running: ', count)
        count -= 1
        time.sleep(0.5)
countdown(9)
print ("The world as you know it has ended!")

