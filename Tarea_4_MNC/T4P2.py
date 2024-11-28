# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:06:13 2022

@author: benja
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

epsilon = 10**-8 #epsilon pequeño
#Defino la funcion y la derivada
def ecc(m,b,h):
    return m - np.tanh(b*m+h)
def eccD(m,b,h):
    return 1 - b*(1/(np.cosh(b*m+h)))**2
#Defino newton 
def Newton(fx,fd,x0,b,h):
    n = x0
    n_1 = n - fx(n,b,h)/fd(n,b,h)
    while abs(n_1-n)>epsilon:
        n = n_1
        n_1 = n - fx(n,b,h)/fd(n,b,h)
    return n_1
#Lista de betas, uno muy cerca de 0 , otro de 10 y el resto mas cerca de 0 que de 9 ( se ven mas bonitos )
B = [0.000001,0.5,1,2.2,9.99]
#Arreglo de campos mag
H = np.linspace(0.001,10,10000)


Graf = [] #En esta lista se juntan todos los m, cada item es una lista que corresponde a las raices para cierto beta
for item in B: #for "grande" es beta
    blist = [] #cada beta es una lista
    for item2 in H: #for chico es h
        r = Newton(ecc,eccD,1,item,item2) #se hace newton
        blist.append(r)
    Graf.append(blist)
    
#Ploteo
fig, ax = plt.subplots()
ax.plot(H, Graf[0], label="e-5")
ax.plot(H, Graf[1], label="0.5")
ax.plot(H, Graf[2], label="1.0")
ax.plot(H, Graf[3], label="2.2")
ax.plot(H, Graf[4], label="9.9")
ax.set_title('m para Beta fijo (Espectro completo)')
plt.xlabel('Campo Magnetico')
plt.ylabel('Magnetización')
plt.legend()

#Se repite lo mismo pero con un rango reducido en h, esto es para hacerle un "zoom" al comportamiento de las raices
H = np.linspace(0.001,0.5,10000)
Graf = []
i = 0
for item in B:
    blist = []
    for item2 in H:
        r = Newton(ecc,eccD,1,item,item2)
        blist.append(r)
    Graf.append(blist)
    
fig, ax = plt.subplots()
ax.plot(H, Graf[0], label="e-5")
ax.plot(H, Graf[1], label="0.5")
ax.plot(H, Graf[2], label="1.0")
ax.plot(H, Graf[3], label="2.2")
ax.plot(H, Graf[4], label="9.9")
ax.set_title('m para Beta fijo (Espectro parcial)')
plt.xlabel('Campo Magnetico')
plt.ylabel('Magnetización')
plt.legend()



        