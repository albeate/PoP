from math import *
from math import atan
import cmath


# This program deals with complex numbers in different ways such as
# finding the modulus and argument,
# and finding the roots of a complex 2nd degree polynomial.




#problem. a)
def cmod(z):
    """
    Calculates the modulus of a complex function, a + ib.

    input: z.real + z.imag*j
    output: modulus
    """
    return (sqrt(z.real**2+z.imag**2))

def carg(z):
    """
    Calculates the argument of a complex function, a + ib.Then divided by cmod(z).

    input: z.real + z.imag*j
    output: z.real/cmod(z) and z.imag/cmod(z) and what quadrant 
    """
    a = z.real
    b = z.imag

    if a > 0:
        return atan(b/a)
    
    elif a < 0 and b >= 0:
        return atan(b/a)+pi
    
    elif a < 0 and b < 0:
        return 2*pi+atan(b/a)-pi
    
    elif a == 0 and b > 0:
        return +(pi/2)
    
    elif a == 0 and b < 0:
        return 2*pi-(pi/2)
    
    elif a == 0 and b == 0:
        return 0

# This "def" calculates |r|=√a**2+b**2, modulus,
# and arctan((a/r)/(b/r)), argument, respectivly. 


        
#problem b)
def csqrt1(z):
    """
    Calculating the square roots of the function w1.

    input: z.rela + z.imag*j 
    output: square root of cmod(z)
    """
    return sqrt(cmod(z))*complex(cos(carg(z)[0]/2.0), sin(carg(z)[0]/2.0))

def csqrt2(z):
    """
    Calculating the square roots of the function w2.

    input: z.real + z.imag*j
    output: square root of cmod(z)
    """
    return sqrt(cmod(z))*complex(cos((carg(z)[0]+2*pi)/2.0), sin(carg(z)[0]/2.0))
                                                
# This "def" calculates the square roots of w1 = √re^iθ/2
# and w2 = √re^iθ*π/2, respectivly.



#problem c)
def polyrod1(z,z1,z2):
    """
    Calculating the roots of a complex function using csqrt1.

    input: z.real + z.imag*j, z1.real + z1.imag*j, z2.real + z2.imag*j
    output: complex root of the complex function
    """
    d = z1**2-4*z*z2
    temp_calc = -z1+csqrt1(d)
    return temp_calc/(2.0*z)
   
        
def polyrod2(z,z1,z2):
    
    """
    Calculating the roots of a complex function using sqrt2.

    input:  z.real + z.imag*j, z1.real + z1.imag*j, z2.real + z2.imag*j
    output: complex root of the complex function
    """
    d = z1**2-4*z*z2
    temp_calc = -z1+csqrt2(d)
    return temp_calc/(2.0*z)
    

# This "def" calculates the roots of a complex 2nd degree polynomial.
# How? By defining "a," "b," and "c" as each their own complex function a + ib
# thus getting the correct results in the form of a real and an imaginary number. 

