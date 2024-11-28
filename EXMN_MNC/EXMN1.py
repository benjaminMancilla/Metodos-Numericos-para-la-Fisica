# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 17:09:41 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

gamma = 0.001
nu = 1.5

h = 500
k = 500
x = np.linspace(0, 1, h)
t = np.linspace(0, 4, k)
deltX = x[1]-x[0]
deltT = t[1]-t[0]
p = ((gamma*deltT)/(2*deltX**2))
q = nu*deltT
A = np.zeros((h,k))

def CONDINICIAL(x):
    e = np.e
    return e**(-x**2/0.1)


for i in range(k):
    A[i][0] = 1
    A[i][h-1] = 0

for i in range(h):
    A[0][i] = CONDINICIAL(x[i])


def Trigo(u):
    Trigo = np.zeros((h,k))
    for j in range(k):
        for i in range(h):
            if j == i:
                Trigo[j][i] = 1+2*p-q*(1-A[u][i])
            elif j == i+1 or j == i-1:
                Trigo[j][i] = -p
            else:
                pass
    return Trigo


def B(u):
    B = np.zeros(k)
    B[0] = A[u][0]+p
    for i in range(1,k):
        B[i] = A[u][i]
    return B


for o in range(k-1):
    A[o+1][:] = np.linalg.solve(Trigo(o),B(o))
    print(o)



for i in range(5):        
    plt.plot(x,A[100*i][:], label = 't =' + str(round(t[100*i],2)))
plt.plot(x,A[k-1][:], label = 't =' + str(round(t[k-1],2)))
plt.xlabel("Posición")
plt.ylabel('Densidad')
plt.title('Fisher KPP')
plt.legend()    
plt.show()