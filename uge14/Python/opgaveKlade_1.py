# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt
from pylab import figure, show, rand
from matplotlib import animation
import random
from math import pi,cos,sin

"""
Aflederingsopgave uge 14
"""

def len_vector(v):
    return np.sqrt(v[0]**2+v[1]**2)

def scale(v,s):
    a = len_vector(v)
    return ((v[0]/a)*s,(v[1]/a)*s)

def vec(p1,p2):
    return ((p2[0]-p1[0]),(p2[1]-p1[1]))

def add(v1,v2):
    return ((v1[0]+v2[0]),(v1[1]+v2[1]),(v1[2]+v2[2]))

def dot(v1,v2):
    return (v1[0]*v2[0]+v1[1]*v2[1])

def proj(p,v):
    a = (dot(p,v))/(len_vecor(v)**2)
    return (a*v[0],a*v[1])

def step(p,v,t_delta):
    p_new=(p[0]+t_delta*v[0],p[1]+t_delta*v[1])
    return(p_new)

def willcolide(p,v,c,r):
    if len_vector(vec(c,step(p,v,t_delta))) > r:  #???
        #den kolliderer
        return True
    else:
        #den kolliderer ikke
        return False


def next_position(p,v,c,r,t_delta):
    #----- den er slet ikke færdig  -----
    if willcolide(p,v,c,r) == True:
        #bestem p
        """
        p1 = p
        (p1 +  vu-c)**2 = r**2
        pc = add(p1,vu)
        p_new = add(pc,scale(v,(len_vector(v)*(1-u)))
        bestem v   Fra nr. 3 a,b,c
        vp = vec(p1,proj(p1,vec(c,pc)))
        p1_m=add<8p1,scale(vp,2*len_vector(vp)))
        v2 = scale(vec(pc,p1_m),len_vector(v))
        v_new = v2
        """
        #snyde beregning her i stedet for det oven over
        v_new =(v[0]*(-1),v[1]*(-1))
        p_new=step(p,v_new,t_delta)
    else:                   # herfra er det rigtigt
        p_new=step(p,v,t_delta)
        v_new = v              #hastighed og retning ændres ikke
    return(p_new,v_new)
             
def beholder_tryk(liste,radius,masse):  #opgave c beregning
    A=pi*radius**2
    N=len(liste)
    #print 'N:',N
    vector_len=0
    #for element in liste:
    #    vector = element[1]
    #    vector_len = vector_len + len_vector(vector)
    vector_len_gns = vector_len/N
    P= N*masse*(vector_len_gns**2)/2*A
    #print 'P:',P
    return P    


def ny_vektor_hastighed(liste, masse,T):   #opgave d beregning - hvor vektor længde skal ændres
    k_b=1.380658*10**(-23)
    N=len(liste)
    vector_len=0
    vector_gns_new = (N*k_b*T*2/N*masse)
    for element in liste:
        vector = element[1]
        vector_len = vector_len + len_vector(vector)
    vector_gns_old = vector_len/N
    factor = vector_gns_new/vector_gns_old
    liste_new=[]
    for element in liste:
        v_new=scale(element[1],factor)
        partikel = [element[0],v_new]
        liste_new.append(partikel[:])
    return liste_new
    

def initier_beholder(antal,radius):
    liste = []
    partikel = []
    v_max = 0.9 #???
    for j in range(antal):
        count = 0
        while count == 0:
            p = (random.uniform(-radius,radius),random.uniform(-radius,radius))
            if len_vector(p) < radius : count = 1
        v_dir  = 2*pi/(j+1)  
        v_long = v_max /(j+1)
        v = (v_long*cos(v_dir),v_long*sin(v_dir))
        partikel = [p,v]
        liste.append(partikel)
    return liste

#Tidsinterval 0<= t_i <=t_max   t_delta
t_max = 1
t_delta = 0.5 # ???? 0.001


# Dan beholder
liste_new=[]
liste_old=[]
antal_partikler = 5  # ???
#partikle_liste = [] # hver med positions og hastigheds vektor #beholder=[]
radius = 10   # ???
c=(0,0)
liste_new = initier_beholder(antal_partikler,radius)

#  -----------------Opgave c -----------------------
m = 10**(-23)
print 'Antal partikler:',antal_partikler,'Beholdertryk:', beholder_tryk(liste_new,radius,m)
#  -----------------Opgave d -----------------------
#
#  -----------------Opgave e -----------------------
#T = 150
#T = 300    #K/ T = 36.85 C
T = 373.15 #K / T = 100 C
#T = 573.15 #K / T = ?

#Delopgave b:
plt.ion()
plt.figure()
plt.xlabel('Beholder radius: 10')
plt.ylabel('Beholder radius: 10')
plt.title('Uge 14 Aflevering ',fontsize=20)
count = 0
while count <150:
    plt.clf()    
    beholder=plt.Circle((0,0),10,color='black',fill=False)
    fig = plt.gcf()
    fig.gca().add_artist(beholder)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    liste_old = liste_new
    liste_new =[]
    count += 1
    nummer = 0

    #Delopgave d:
    liste_mod_vec = ny_vektor_hastighed(liste_old,m,T)
    for element in liste_mod_vec:
        nummer = nummer+1
        p_old=element[0]
        v_old=element[1]
        if nummer == 1:
            plt.plot(p_old[0], p_old[1], '+',color='r')
            plt.draw()
        if nummer == 2:
            plt.plot(p_old[0], p_old[1], '*',color='blue')
            plt.draw()
        if nummer == 3:
            plt.plot(p_old[0], p_old[1], '+',color='blue')
            plt.draw()
        if nummer == 4:
            plt.plot(p_old[0], p_old[1], '.',color='black')
            plt.draw()
        if nummer == 5:
            plt.plot(p_old[0], p_old[1], '+',color='green')
            plt.draw()
        p_new,v_new = next_position(p_old,v_old,c,radius,t_delta)
        partikel_new=[p_new,v_new]
        liste_new.append(partikel_new)
plt.ioff()

