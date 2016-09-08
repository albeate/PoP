# -*- coding: utf-8 -*-
# assigment due 12th of December 2014
from __future__ import division
import matplotlib.pyplot as plt
import time

star = "*"

print 'Time it takes the program to run:'
time = time.clock()
print time
print star*20


class Dataset(object):
        """manages a variable with observational data"""
        def __init__(self, x = [], y = []):
                self.x = x
                self.y = y
                if len(self.x) != len(self.y):
                        raise ValueError ('Not of same lenght')		

        def __str__(self):
                """ 
                        input: two list such as: x and y
                        output: string of the two lists
                """
                return str(self.x) + '\n' + str(self.y)

        def __len__(self):
                """ returns the lenght of the list"""
                return len(self.x)

        def __getitem__(self, i):
                """ it UDLÆSER. take it!"""
                if isinstance(i, int):
                        if i >= len(self.x):
                                raise IndexError ('Out of range')
                        elif i == 0:
                                return self.x
                        elif i == 1:
                                return self.y
                        else:
                                raise ValueError ("nope!")
                else:
                        raise TypeError('Wrong type')

        def __setitem__(self, i, value):
                if isinstance(i, (list,tuple)):
                        self.x[i] = value[0]
                        self.y[i] = value[1]
                else:
                        raise TypeError ("Not a tuple or list")
                

        def readDataPoints(self, filePath): 
                """ reads the data into two list """
                try:
                        fi = open(filePath, "U")
                except IOError:
                        print "Error no. 1 from read from file: "+str(filePath)+" does not exits!"
                        raise SystemExit()
                with open(filePath, "r") as f:
                        for line in f:
                                try:
                                        x,y = map(float, line.split(','))
                                except ValueError:
                                        print "Error no. 2 from read from file: "+str(filePath)+" data is not usable"
                                        raise SystemExit()
                                        
                                x,y = map(float, line.split(','))
                                try:
                                        1/y
                                except:
                                        print "Fejl nr. 3 from read from file: "+str(filePath)+" data is not usable"
                                        raise SystemExit()
                                self.x.append(x)
                                self.y.append(y)              
                return  ([self.x, self.y])
        
class Regression(object):
        """manages a variable data of the type Dataset"""
        def __init__(self, data):
                self.data = data
                try:
                        self.x_mean = sum(data[0])/len(data) # calculates the mean value of x
                        self.y_mean = sum(data[1])/len(data) # calculates the mean value of y

                        SAK = sum(map(lambda x: (x-self.x_mean)**2, self.data[0])) # the sum of deviations of the squares
                        SAP = sum(map(lambda x,y: (x-self.x_mean)*y, self.data[0],self.data[1])) # the sum of deviations of the products
                        a = SAP/SAK
                        self.a = a
                except:
                        raise ValueError ("can't divide by zero")

        def f(self, b):
                """ Calculates a linear line
                        output: linear line 
                """
                return self.a*(b-self.x_mean)+self.y_mean

        def linearAnalysis(self):
                """ Calculates max and min of x and f(x), respectivly. 
                        output: two lists 
                """
                return ([max(self.data[0]), min(self.data[0])],[self.f(max(self.data[0])), self.f(min(self.data[0]))])

        def plot(self):
                plt.figure()
                plt.grid()
                funktion = self.linearAnalysis()
                plt.plot(funktion[0], funktion[1], color='cyan')
                plt.scatter(self.data[0],self.data[1], color='red')
                plt.xlabel("Hatching time in hours, x")
                plt.ylabel("Humidity in %, f(x)")
                plt.show()

data = Dataset()
print "flueaeg " + str(data.readDataPoints("flueaeg.txt"))
print star*20
minmax = Regression(data)
print "max, min of x, and max, min of f(x), respectivly: " + str(minmax.linearAnalysis())
b = Regression(data) 
b.plot()
print '---------------------------------'
print 'Testing whether the code can handle errors in the data:'
print "Test of character between columns, when not comma "+ str(data.readDataPoints("Flueaeg1 med forkert skilletegn.txt"))
#print "Test different number of columns in the file " + str(data.readDataPoints("flueaeg - forskellig antal.txt"))
#print "Test of zerro in the colums as measuring points " + str(data.readDataPoints("talNul.txt"))
#print "Test when the files does not excist /n " + str(data.readDataPoints("flueaegxxx.txt"))


