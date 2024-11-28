# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 23:49:56 2022

@author: benja
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import fmin

#Importo los datos
i = 0
for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       
       if i==0:
           Col1 = []
           Col2 = []

           for linea in f:
               x = linea.split("  ")
               primerdato = x[0][:-1]
               segunddato = x[1]
               Col1.append(float(primerdato))
               Col2.append(float(segunddato))
           f.close()
           archv = [np.array(Col1),np.array(Col2)]
           archvB = [(Col1),(Col2)]
           i += 1
           
       else:
           break
       

#Defino la funcion gausseana y las que determinan el error del fiteo para cada funcion
def gauss(x,a,mu,sigma):
    return a*np.exp(-(x-mu)**2/(2*sigma**2))

def errorRecta(p):
    a, b = p
    lista = archv
    xi = lista[0]
    yi = lista[1] 
    suma = []
    U = np.arange(0,len(xi),1)
    for u in U:
        termino = (yi[u]-(a*xi[u]+b))**2
        suma.append(termino)
    return sum(suma)


def errorGauss(p):
    a, b = p
    lista = archv
    xi = lista[0].tolist()
    yi = lista[1].tolist()
    suma = []
    U = np.arange(0,len(xi),1)
    for u in U:
        termino = (yi[u]-(a*gauss(xi[u],3.1e-16-1.55e-16,5135.9,2.2)+b*gauss(xi[u],6.4e-16-1.55e-16,5185.5,2.2)))**2
        suma.append(termino)
    return sum(suma)

#Minimizo las funciones de error para calcular los parametros optimos
fxd = fmin(errorGauss,[2,4])
fxu = fmin(errorRecta,[0,1.4e-16])

optimalgauss1 = [3.1e-16-1.55e-16,5136.11300378976,2.2] #No es necesario calcular los parametros optimos
optimalgauss2 = [6.4e-16-1.55e-16,5186.08164104976,2.2] #Para la gausseana ya que no es lineal
#Ploteo
def ploteo(lista):
    plot = []
    for i in lista:
        if fxd[0]*gauss(i,optimalgauss1[0],optimalgauss1[1],optimalgauss1[2])+fxd[1]*gauss(i,optimalgauss2[0],optimalgauss2[1],optimalgauss2[2]) < fxu[0]*i+fxu[1]:
            
            plot.append(fxd[0]*gauss(i,optimalgauss1[0],optimalgauss1[1],optimalgauss1[2])+fxd[1]*gauss(i,optimalgauss2[0],optimalgauss2[1],optimalgauss2[2]))
        else:
            plot.append(fxu[0]*i+fxu[1])
            
    return plot
            
fig, ax = plt.subplots()
ax.set_title("Fiteo")
plt.plot(archv[0], archv[1], 'b+:', label='data')
plt.plot(archv[0], ploteo(archv[0]), 'r-', label='fit')
plt.xlabel('Longitud de Onda en metros')
plt.ylabel('Frecuencia en Hertz')    
plt.legend()
plt.show()










 
            
        