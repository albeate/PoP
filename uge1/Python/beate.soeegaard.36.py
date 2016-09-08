#Find rødderne til et 2. gradspolynomium

from math import sqrt
#For at gøre det lettere at læse og skrive koden.
#Den sørger for at jeg ikke behøver at skrive math.sqrt
#hver gang jeg skal tage kvadratroden af noget.



a = float(input("What is a?:"))
b = float(input("What is b?:"))
c = float(input("What is c?:"))
#Lavede det om til en float i tilfældet af decimalerog
#sørget for at gøre det til et input så vi selv kan bestemme værdien.


d = (b**2) - 4*a*c

#Fortæller at der ingen rødder er til polynomium og slutter programmet. 
if d < 0:
    print ("no real solutions") 

#Men hvis d er større end nul går programmet vider
#med resten af koden som regner hhv x1 og x2 ud.
else:

    if b < 0:
        x1 = (-b+(sqrt((b**2)-(4*a*c)))/(2*a))
    else:
        x1 = (-b-(sqrt((b**2)-(4*a*c)))/(2*a))

    if x1 == 0:
        x2 = (-b/a)
    else:
        x2 = (c/a)/x1
        print ("The roots are: ", x1, x2)
        
#Her har jeg sat programmet til at finde vertex'en som er hhv. det højeste og
#det laveste sted på polynomiumet. 
    if a != 0:
        v = ((-b)/(2*a))
        print("The vertex is:", v)
    else:
        print ("Discriminant is negative")



