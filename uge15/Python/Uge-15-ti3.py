# -*- coding: utf-8 -*-
import re
import numpy as np
import matplotlib.pyplot as plt

import pylab as pl
import datetime

tegn=[];antal=[]
data = {}

def sorter(tegn_streng):   #dict kan kun læse 2 kolonner ind fra regneark
    dict_data = {}
    for element in tegn_streng:  #Så har vi allerede det tegn mindst 1 gang
        if element in dict_data:
            gem = dict_data[element]
            dict_data[element]=gem+1
        else:                       #vi sætter et nyt element ind i dict       
            dict_data[element] = 1
    return dict_data


def data_ud_af_dict(Sorteret_streng):
    xr = Sorteret_streng.keys() #Så har vi en liste over nøgler
    yr = Sorteret_streng.values() #Så har vi en liste over værdier
    return xr,yr 


def plot_diagram(dat_liste):  #Bliver kaldt med liste af lister [[...],[...]]
    tegn = dat_liste[0]
    antal = dat_liste[1]    
    fig = plt.figure()
    width = .1
    ind_space = np.arange(len(antal)) # Her beregnes de antal søjer som der skal printes
    plt.bar(ind_space, antal)
    plt.xticks(ind_space + width / 2, tegn) # Her skriver vi på x akse hvad det er der er tastet/målt
    fig.autofmt_xdate()
    plt.ylabel('y akse tekst')
    plt.xlabel('x akse tekst')
    plt.title("Uge 15 - Opgave tirsdag opgave 3")
    plt.show()
    #plt.savefig("figure.pdf")
    return

taste = raw_input("Indtast data:")
print taste
antal_ialt=len(taste)
data = sorter(taste)
print data
tegn,antal = data_ud_af_dict(data)
print tegn, antal
plot_diagram(data_ud_af_dict(data))


