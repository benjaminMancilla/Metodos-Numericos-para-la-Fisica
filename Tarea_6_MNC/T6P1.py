# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:44:41 2022

@author: benja
"""

import numpy as np
import sympy as sp
from scipy.linalg import hilbert
import time
import matplotlib.pyplot as plt
n = 20 #Numero de particiones
Ns = np.linspace(1,105,n).astype('int') #Espacio para los calculos (hasta un poco mas de 100)

#Creo el vector b 
def bVector(n):
    b = []
    for i in range(1,n+1):
        element = 1/i
        b.append(element)
    b = np.array(b).reshape(n, 1)
    
    return b

#Creo las listas vacias para los tiempos y los errores
tiemposGE=np.empty(n)
tiemposLU=np.empty(n)
errorGE = np.empty(n)
errorLU = np.empty(n)

#Comienzo la iteraciones para cada particion
for i in range(n):
    A=hilbert(Ns[i]) #Defino la matriz de Hilbert mediante librerias
    B=bVector(Ns[i]) #Calculo el vector b para el caso
    solAnalit = (np.zeros(Ns[i]).reshape((Ns[i],1))) #La solucion esperada
    solAnalit[0] = 1 #El primero termino es 1


    AM=sp.Matrix(A) #Paso las matrices a sympy Matrix
    BM=sp.Matrix(B)
    #-----------------------------------------------------
    startGE=time.perf_counter() #Empiezo a contar para GE
    Ainv_GE=AM.inv(method = "GE") #Invierto mediante GE
    x_GE=(np.array(Ainv_GE.dot(BM))).reshape((Ns[i],1)) #Calculo solucion mediante producto punto
    endGE=time.perf_counter() #Una vez hechos los calculos termino el contandor para GE
    startLU=time.perf_counter() #El proceso es analogo para LU
    Ainv_LU=AM.inv(method = "LU")
    x_LU=(np.array(Ainv_LU.dot(BM))).reshape((Ns[i],1)) #Paso los resultados a arrays porque me parece mas comodo
    endLU=time.perf_counter()
    
    tiemposGE[i]=endGE-startGE #El tiempo total es el inicial menos el final
    tiemposLU[i]=endLU-startLU
    eg = solAnalit - x_GE #Calculo de la matriz error, es decir, componente calculado vs esperado
    el = solAnalit - x_LU
    EG = 0
    EL = 0
    for j in range(eg.size): #Hago la sumatoria para calcular el error cuadratico
        EG += ((eg[j][0])**2)/eg.size
        EL += ((el[j][0])**2)/el.size
        
    errorGE[i] = EG ##Agrego los errores
    errorLU[i] = EL

#Ploteo
plt.semilogy(Ns,tiemposGE,label='Eliminacion de Gauss')
plt.semilogy(Ns,tiemposLU,label='Descomposicion LU')
plt.xlabel('N')
plt.ylabel('tiempo [s]')
plt.legend()
plt.show()
plt.semilogy(Ns,errorGE,label='Eliminacion de Gauss')
plt.semilogy(Ns,errorLU,label='Descomposicion LU')
plt.xlabel('N')
plt.ylabel('error')
plt.legend()
plt.show()


