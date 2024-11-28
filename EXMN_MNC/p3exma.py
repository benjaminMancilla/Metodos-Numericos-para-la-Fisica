# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 18:10:49 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as alg
plt.style.use('dark_background')

#El desarrollo es igual a la p1 entonces copiamos y pegamos
#Cambia el p y ademas la condiciones de borde
#Tambien cambia el B, ya que en vez de ser b+detlT(nu*n-nu*n**2)



h = 100
k = 100
x = np.linspace(-50, 50, h)
t = np.linspace(0, 8, k)
deltX = x[1]-x[0]
deltT = t[1]-t[0]
p = ((1j*deltT)/(4*(deltX**2)))
q = deltT*1j
A = np.zeros((h,k),dtype=np.complex_)

def CONDINICIAL(x):
    return np.e**(-(x**2)/0.5**2) * np.e**(x*1j)

def Vo(x):
    
    if (2<=x and x<=4):
        return 2
    else:
        return 0



for i in range(h):
    A[0][i] = CONDINICIAL(x[i])


def K(u):
    Trigo = np.zeros((h,k),dtype=np.complex_)
    for j in range(k):
        for i in range(h):
            if j == i:

                Trigo[j][i] = 1+2*p
            elif j == i+1 or j == i-1:
                Trigo[j][i] = -p
            else:
                pass
    return Trigo


def B(u):
    B = np.zeros((h,k),dtype=np.complex_)
    for j in range(k):
        for i in range(h):
            if j == i:

                B[j][i] = 1-2*p
            elif j == i+1 or j == i-1:
                B[j][i] = p
            else:
                pass
    return B

def Fn(u):
    fn = np.zeros(k)
    for i in range(k):
        fn[i] = -1j*deltT*Vo(x[i])*A[u][i]
        
    return fn
        
    


for o in range(k-1):
    A[o+1][:] = alg.solve(K(o), B(o)@A[o] + Fn(o))
    plt.plot(x,np.absolute(A[o+1][:])**2)
    plt.show()


    





XX = []
TT = []
DD = []
for o in range(len(t)):
    for d in range(len(x)):
        XX.append(x[d])
        TT.append(t[o])
        DD.append((np.absolute(A[o][d])))
        

plt.scatter(XX,TT, s=1, c=DD, cmap = "plasma")
plt.xlabel("Posición")
plt.ylabel('Tiempo')
plt.show()

plt.plot(x,np.absolute(A[99][:])**2, label = 't =' + str(round(t[99],2)))
plt.show()
        
        
    


