from __future__ import division
import pygame, sys,pygame.mixer
import math
import pylab
import numpy as np
import time
import random
from pygame.locals import*
pygame.init()

"""basic variables"""
clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 17)
edgeX,edgeY = 10,10
boxWidth,boxHeight = 950,680
size = width,height = 1000,700
centerX,centerY=int(width/2),int(height/2)
screen = pygame.display.set_mode(size)
x,y = width/2, height/2
radius = 3
number_of_atoms =200
position = []
v = []
color = []

"""set initial positions and velocities"""

for j in range(number_of_atoms):
    position.append([400+random.randint(-250,320),325+random.randint(-285,375),0])
    v.append([random.uniform(-5,5),random.uniform(-5,5)])
    m.append(1)
    color.append((0,0,255))
color[number_of_atoms-1]=((250,0,0))
for i in range(4):
 v.append([0,0])

def colission(a,v,b): # a - list of all atoms, v - list of all velocites (atom j has in position position[j] and travel with velocity v[j]), b - the atom we check for collisions
 for ball in a:
  if ball is not b:
   distanceX,distanceY = (b[0]-ball[0]),(b[1]-ball[1])
   distance = distanceX*distanceX + distanceY*distanceY
   if distance < 36: #radius=3,(2radius)**2=36
    ma,mb=1,1 #the mass of all atoms is 1
    i,j = a.index(ball),a.index(b)
    change = [-0.15*distanceX,-0.15*distanceY]

    Vax,Vay = v[i][0],v[i][1]
    Vbx,Vby = v[j][0],v[j][1]

    Angle =math.atan2(distanceY,distanceX) # math.acos((distanceX/distance))
    cos,sin = math.cos(Angle),math.sin(Angle)

    #changing coordiantes:
    vg,vh=[Vag,Vah],[Vbg,Vbh]=[Vax*cos+Vay*sin,Vay*cos-Vax*sin],[Vbx*cos+Vby*sin,Vby*cos-Vbx*sin]

    #after collision:
    Va2,Vb2=(2*mb*Vbg)/(ma+mb), (2*ma*Vag)/(ma+mb) #because ma=mb the term (ma-mb)*Vag or (mb-ma)*Vbg  cancels out

    v1,v2 = [Va2,Vah] , [Vb2,Vbh]
    #changing coordiantes again:
    sin = -sin
    v1,v2 =  [(Va2*cos+Vah*sin),Vah*cos-Va2*sin], [v2[0]*cos+v2[1]*sin,v2[1]*cos-v2[0]*sin]
    v[j],v[i]= v2,v1 #update velocites
    a[i][0],a[i][1]=a[i][0] + change[0], a[i][1] + change[1] #treating overlaps
    return()

"""the loop"""

while 1:
    screen.fill((0,0,0))

    mouseX,mouseY=pygame.mouse.get_pos()
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
     elif event.type == MOUSEBUTTONDOWN:
        if mouseY<edgeY+50 and mouseY>edgeY-50 and mouseX<edgeX+boxWidth and mouseX>edgeX-50:
         z=1
     elif event.type == MOUSEBUTTONUP:
        z=0
    if z==1:
        dy = mouseY-edgeY
        boxHeight = boxHeight-dy
        edgeY=mouseY

    pygame.draw.rect(screen, (200,100,0), (edgeX,edgeY,boxWidth,boxHeight),1)
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        sys.exit()

    for j in range(len(position[:number_of_atoms])):
        colission(position,v,position[j]) #check for collisions
        position[j][0]+=v[j][0] 
        position[j][1]+=v[j][1]

        """checking for collisions with the walls"""
        if position[j][0]+radius>edgeX+boxWidth:
         
         v[j][0]=-1*(v[j][0])
         position[j]=[(-radius+edgeX+boxWidth)-2,position[j][1],0]

        if position[j][0] - radius<edgeX:
         
         v[j][0]=-1*(v[j][0])
         position[j]=[radius+edgeX+2,position[j][1],0]

        if position[j][1]+radius>edgeY+boxHeight:
        
         v[j][1]=-1*(v[j][1])
         position[j]=[position[j][0],(-radius+edgeY+boxHeight)-2,0]

        if position[j][1]-radius<edgeY:
       
         v[j][1]=-1*(v[j][1])
         position[j]=[position[j][0],edgeY+2+radius,0]

    clock.tick(40)
    for i in range(len(position[:number_of_atoms])):
     circle = pygame.draw.circle(screen,color[i], (int(position[i][0]),int(position[i][1])),radius)
    pygame.display.flip()
 