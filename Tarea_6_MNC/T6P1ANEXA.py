# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 22:20:34 2022

@author: benja
"""

import numpy as np
import sympy as sp
from scipy.linalg import hilbert
from numpy.linalg import inv
import time
import matplotlib.pyplot as plt
#P1

#Creo el vector b 
def bVector(n):
    b = []
    for i in range(1,n+1):
        element = 1/i
        b.append(element)
    b = np.array(b).reshape(n, 1)
    
    return b

 
#Defino Hilbert a mano (no queria usar libreras)
#Basicamente solo calculo el valor de las diagonales y luego voy diagonal por diagonal
#insertando los datos, osea en vez de calcular n*n calculo 2n-1.
#ACTUALIZACION: aunque mi funcion sea un poco mas lenta que la de libreria, con grandes
#N aporta mucha demora, lamentablemente es bastante complicado optimizar la funcion
#tal cual como scipy :c
def H(n):
    up = []
    down = []
    dig = 1/(n)
    for i in range(n-1):
        up.append(1/(i+1))
        down.append(1/(n+i+1))
    up.reverse()
    dat = [up,down]
    mat = np.zeros([n,n])
    for k in range(2):
        for i in range(n-1):
            rng = np.arange(n-1-i)
            mat[rng, rng+1+i] = dat[k][i]
        mat = np.rot90(mat,2)
            
    np.fill_diagonal(mat, dig)
    mat = np.rot90(mat)
    
   
    return mat


  
#Se invierte la matriz para calcular x mediante Gauss
def HGauss(n):
    x = np.zeros(n)
    A = np.concatenate((hilbert(n), bVector(n)),axis=1)
  
    #Implemento Gauss e invierto la matriz
    for i in range(n):
     
        for j in range(i+1, n):
            r = A[j][i]/A[i][i]
        
            for k in range(n+1):
                A[j][k] = A[j][k] - r * A[i][k]

    # calculo los x
    for i in range(n-2,-1,-1): #Recorro desde el ultimo hasta el primero
        x[i] = A[i][n] #Es -2 y no -1 porque partimos de la segunda fila
    
        for j in range(i+1,n): #Recorro las columnas
            x[i] = x[i] - A[i][j]*x[j] #Hago la resta
        x[i] = x[i]/A[i][i] #Y luego divido por el factor
    return x



    
#Funcion que calcula ambas triangulares (auxiliar)
#Primer paso de LU
def lu(M):
    
    #Numero de filas
    n = M.shape[0]
    
    U = M.copy() #U es una copia de A
    L = np.eye(n, dtype=np.double) #L parte como la identidad
    
    #Corro las filas
    for i in range(n):
            
        f = U[i+1:, i] / U[i, i] #Por cuanto tengo que multiplicar
        
        L[i+1:, i] = f #Multiplico en L
        print(U)
        U[i+1:] -= f[:, np.newaxis] * U[i] #Resto
        print(U)
        
    return L, U


def SolveLU(L,U,b):
    L = np.array(L, float)
    U = np.array(U, float)
    b = np.array(b, float)
    n,_ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)
    
    #Forward
    for i in range(n):
        sumj = 0
        for j in range(i):
            sumj += L[i,j] * y[j]
        y[i] = (b[i]-sumj)/L[i,i]
    #Backward
    for i in range(n-1,-1,-1):
        sumj = 0
        for j in range(i+1,n):
            sumj += U[i,j] * x[j]
        x[i] = (y[i]-sumj)/U[i,i]
    return x

n = 2
Ns=np.linspace(1,4,n).astype('int')
tiemposGE=np.empty(n)
tiemposLU=np.empty(n)

for i in range(n):
    A = hilbert(Ns[i])
    b = bVector(Ns[i])
    L = lu(A)[0]
    U = lu(A)[1]
    startGE=time.perf_counter()
    x_GE=HGauss(Ns[i])
    endGE=time.perf_counter()
    startLU=time.perf_counter()
    x_LU=SolveLU(L,U,b)
    endLU=time.perf_counter()
    #if Ns[i]%10==0: 
       # print('x_GE(N='+str(Ns[i])+')=',x_GE)
        #print('x_LU(N='+str(Ns[i])+')=',x_LU)
    tiemposGE[i]=endGE-startGE
    tiemposLU[i]=endLU-startLU

plt.semilogy(Ns,tiemposGE,label='Eliminacion de Gauss')
plt.semilogy(Ns,tiemposLU,label='Descomposicion LU')
plt.xlabel('N')
plt.ylabel('tiempo [s]')
plt.legend()
    