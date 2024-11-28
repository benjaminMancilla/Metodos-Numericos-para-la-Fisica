# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:54:29 2022

@author: benja
"""
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#Defino las constantes
N = 100
fcte = 0.01
k = 1
m = 1
lo = 0.1
w = k/m

#Primero haremos el caso con 2 bordes

#Creo las matrices vacias para rellenarlas despues
RSB = np.zeros((N,N))
F1 = np.zeros(N).reshape(N,1)
F2 = np.zeros(N).reshape(N,1)
F3 = np.zeros(N).reshape(N,1)
L0 = np.zeros(N).reshape(N,1)
#Numero de ecuaciones
Nn = sp.Matrix(np.arange(1,101,1))
Nu = sp.Matrix(np.arange(1,100,1))
#Relleno todas las matrices 
#RSB es una trigonal ya que el patron se repite siempre excepto para el primera y ultima
# ecuacion, ya que son las esquinas
#El resto es rellenar con los datos que se piden en el enunciado (fuerzas)
for i in range(N):
    if i == 0:
        RSB[i][i] = 2
        RSB[i][i+1] = -1
        F1[i][0] = fcte
        F2[i][0] = 0.0002*(i+1)
        F3[i][0] = (6*(10**(-6)))*(i+1)*(99-i)
        L0[i][0] = lo*(i+1)
    elif i == N-1:
        RSB[i][i] = 2
        RSB[i][i-1] = -1
        F1[i][0] = fcte
        F2[i][0] = 0.0002*(i+1)
        F3[i][0] = (6*(10**(-6)))*(i+1)*(99-i)
        L0[i][0] = lo*(i+1)
    else:
        RSB[i][i] = 2
        RSB[i][i+1] = -1
        RSB[i][i-1] = -1
        F1[i][0] = fcte
        F2[i][0] = 0.0002*(i+1)
        F3[i][0] = (6*(10**(-6)))*(i+1)*(99-i)
        L0[i][0] = lo*(i+1)
   
#Recordamos que factorizamos el -k (los simbolos estan invertidos en la matriz), en
#este caso no hace diferencia ya que vale 1, pero hay que generalizar.
RSB = RSB*k
print(RSB)
#Pasamos las matrices a sympy
RSB = sp.Matrix(RSB)
F1 = sp.Matrix(F1)
F2 = sp.Matrix(F2)
F3 = sp.Matrix(F3)
F = [F1,F2,F3]
#Invertimos RSB
invt = RSB.inv()
sol = ["f constante","f lineal","f cuadratico"]
#Calculamos las soluciones para cada caso y ploteamos
for i in range(3):
    fig, ax = plt.subplots()
    ax.set_title(sol[i])
    sol[i] = (invt*F[i]) 
    plt.plot(Nn, sol[i], 'b+:')
    plt.xlabel('N')
    plt.ylabel('Posicion con bordes')    
    plt.legend()
    plt.show()
sol = ["f constante","f lineal","f cuadratico"] 
for i in range(3):
    S = (invt*F[i]) 
    SS = np.zeros(N-1).reshape(N-1,1)
    for j in range(N-1):
        SS[j] = S[j+1] - S[j]
    
    fig, ax = plt.subplots()
    ax.set_title(sol[i])  
    plt.plot(Nu, SS, 'b+:')
    plt.xlabel('N')
    plt.ylabel('Enlongacion con bordes')    
    plt.legend()
    plt.show()

RCB = np.zeros((N,N))
F1 = np.zeros(N).reshape(N,1)
F2 = np.zeros(N).reshape(N,1)
F3 = np.zeros(N).reshape(N,1)
L0 = np.zeros(N).reshape(N,1)
Nn = sp.Matrix(np.arange(1,101,1))
for i in range(N):
    if i == 0:
        RCB[i][i] = 2
        RCB[i][i+1] = -1
        F1[i][0] = fcte
        F2[i][0] = 0.0002*(i+1)
        F3[i][0] = (6*(10**(-6)))*(i+1)*(99-i)
        L0[i][0] = lo*(i+1)
    elif i == N-1:
        RCB[i][i] = 1
        RCB[i][i-1] = -1
        F1[i][0] = fcte
        F2[i][0] = 0.0002*(i+1)
        F3[i][0] = (6*(10**(-6)))*(i+1)*(99-i)
        L0[i][0] = lo*(i+1)
    else:
        RCB[i][i] = 2
        RCB[i][i+1] = -1
        RCB[i][i-1] = -1
        F1[i][0] = fcte
        F2[i][0] = 0.0002*(i+1)
        F3[i][0] = (6*(10**(-6)))*(i+1)*(99-i)
        L0[i][0] = lo*(i+1)
        
RCB = RCB*k

RCB = sp.Matrix(RCB)
F1 = sp.Matrix(F1)
F2 = sp.Matrix(F2)
F3 = sp.Matrix(F3)
F = [F1,F2,F3]
invt = RCB.inv()
sol = ["f constante","f lineal","f cuadratico"]
for i in range(3):
    fig, ax = plt.subplots()
    ax.set_title(sol[i])
    sol[i] = (invt*F[i]) 
    plt.plot(Nn, sol[i], 'r+:')
    plt.xlabel('N')
    plt.ylabel('Posicion con borde libre')    
    plt.legend()
    plt.show()
sol = ["f constante","f lineal","f cuadratico"] 
for i in range(3):
    S = (invt*F[i]) 
    SS = np.zeros(N-1).reshape(N-1,1)
    for j in range(N-1):
        SS[j] = S[j+1] - S[j]
    
    fig, ax = plt.subplots()
    ax.set_title(sol[i])  
    plt.plot(Nu, SS, 'r+:')
    plt.xlabel('N')
    plt.ylabel('Posicion con borde libre')    
    plt.legend()
    plt.show()
    

    
    
    
    






        
        
        
    