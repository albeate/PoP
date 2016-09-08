from __future__ import division
from math import *
import matplotlib.pyplot as plt
#Aflevering nr. 6 i uge 7 af Beate Soeegaard, Freja Lauritsen og Sarah Hansen

def linspace(a,b,n):
    delta = (b-a)/n
    return[i*delta+a for i in range(n)]

def rInt(f,a,b,n):
    lin = linspace(a,b,n)
    delta = (b-a)/n
    liste = map(lambda x: delta*f(x),lin)
    return sum(liste)

def rIntMid(f,a,b,n):
    lin = linspace(a,b,n)
    delta = (b-a)/n
    liste = map(lambda x: delta*0.5*(f(x)+f(x+delta)),lin)
    return sum(liste)

#testning af funktionerne 
g = lambda x: cos(x)
v = lambda x: (1/sqrt(2*pi)*(exp(-x**2/2)))
p = lambda x: sin(1/x)
n = 1000


print "TEST1 af rInt(f,a,b,n)"
print 
print "Integralet af cos(x) i intervallet [0.0,2*pi]:"
print rInt(g,0.0,2*pi,n)
print "Integralet af (1/sqrt(2*pi)*(exp(-x**2/2))) i intervallet [-10.0,10.0]:"
print rInt(v,-10.0,10.0,n)
print "Integralet af sin(1/x) i intervallet [0.001,10.0]:"
print rInt(p,0.001,10.0,n)
print

print "TEST2 af rIntMid(a,b,f,n)"
print 
print "Integralet af cos(x) i intervallet [0.0,2*pi]:"
print rIntMid(g,0.0,2*pi,n)
print "Integralet af (1/sqrt(2*pi)*(exp(-x**2/2))) i intervallet [-10.0,10.0]:"
print rIntMid(v,-10.0,10.0,n)
print "Integralet af sin(1/x) i intervallet [0.001,10.0]:"
print rIntMid(p,0.001,10.0,n)

w = range(1,10)
valet = [rInt(g,0.0,2*pi,i) for i in w]
plt.plot(w,valet)
valto = [rIntMid(g,0.0,2*pi,j) for j in w]
plt.plot(w,valto)
plt.xlabel('(n'','' n)')
plt.ylabel('(rIntMid(f,a,b,j)'','' rInt(f,a,b,n))')
plt.title('Opg. d - graf g')
plt.show()

w = range(1,10)
valet = [rInt(v,-10.0,10.0,i) for i in w]
plt.plot(w,valet)
valto = [rIntMid(v,-10.0,10.0,j) for j in w]
plt.plot(w,valto)
plt.xlabel('(n'','' n)')
plt.ylabel('(rIntMid(f,a,b,j)'','' rInt(f,a,b,n))')
plt.title('Opg. d - graf v')
plt.show()

w = range(1,1000)
valet = [rInt(p,0.001,10.0,i) for i in w]
plt.plot(w,valet)
valto = [rIntMid(p,0.001,10.0,j) for j in w]
plt.plot(w,valto)
plt.xlabel('(n'','' n)')
plt.ylabel('(rIntMid(f,a,b,j)'','' rInt(f,a,b,n))')
plt.title('Opg. d - graf p')
plt.show()

if __debug__:
    print "Test af rInt"
    print "Test1 af g= ", rInt(g,0,2*pi,1000) < 0.01
    print "Test2 af v= ", abs(rInt(v,-10.0,10.0,1000))-1 < 0.1
    print "Test3 af p= ", abs(rInt(p,0.001,10,100000) - 2.726201989) < 0.001
    print
    print "Test af rIntMid"
    print "Test1 af g= ", rIntMid(g,0,2*pi,1000) < 0.01
    print "Test2 af v= ", abs(rIntMid(v,-10.0,10.0,1000))-1 < 0.1
    print "Test3 af p= ", abs(rIntMid(p,0.001,10,100000) - 2.726201989) < 0.001

