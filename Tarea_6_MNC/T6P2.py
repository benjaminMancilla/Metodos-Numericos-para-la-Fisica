# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 04:17:16 2022

@author: benja
"""

from numpy import cos, sin, pi
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#Defino ctes y la matriz A y b
g = 10
m1 = 0
m2 = 1
m = 4
c1 = cos(pi/4)
c2 = cos(pi/6)
c3 = cos(pi/12)
s1 = sin(pi/4)
s2 = sin(pi/6)
s3 = sin(pi/12)
F1=m1*g
F2=m2*g
F3=m*g
Y1 = [c1,c1,0,0,0,0,-c2,0,0,0,0,0]
Y2 = [0,0,c1,c1,0,0,0,-c2,-c2,0,0,0]
Y3 = [0,0,0,0,c1,c1,0,0,0,-c2,0,0]
Y4 = [0,0,0,0,0,0,c2,c2,0,0,-c3,0]
Y5 = [0,0,0,0,0,0,0,0,c2,c2,0,-c3]
Y6 = [0,0,0,0,0,0,0,0,0,0,c3,c3]
X1 = [-s1,s1,0,0,0,0,s2,0,0,0,0,0]
X2 = [0,0,-s1,s1,0,0,0,-s2,s2,0,0,0]
X3 = [0,0,0,0,-s1,s1,0,0,0,-s2,0,0]
X4 = [0,0,0,0,0,0,-s2,s2,0,0,s3,0]
X5 = [0,0,0,0,0,0,0,0,-s2,s2,0,-s3]
X6 = [0,0,0,0,0,0,0,0,0,0,-s3,s3]

A = np.array([X1,X2,X3,X4,X5,X6,Y1,Y2,Y3,Y4,Y5,Y6])
b = np.array([[0],[0],[0],[0],[0],[0],[0],[0],[0],[F1],[F2],[F3]])
AM = sp.Matrix(A)
bm = sp.Matrix(b)
#Calculo LU
Ainv_LU=AM.inv(method = "LU")
M1 = np.linspace(0,2,100).tolist()
MAX = []
for i in M1:
    m1 = i
    F1 = m1*g
    b = np.array([[0],[0],[0],[0],[0],[0],[0],[0],[0],[F1],[F2],[F3]])
    bm = sp.Matrix(b)
    sol = Ainv_LU@bm
    soll = np.array(sol.tolist())
    maximo = np.amax(soll)
    MAX.append(maximo)
    
fig, ax = plt.subplots()
ax.set_title("Máximo de la soluciones")
plt.plot(M1, MAX, 'b+:', label='maximos')
plt.xlabel('Tension en Newton')
plt.ylabel('Masa en kilos')    
plt.legend()
plt.show()

    
    
