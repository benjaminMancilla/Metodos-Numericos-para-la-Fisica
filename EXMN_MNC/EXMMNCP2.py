# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:04:52 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')




#P2#

R_1 = 1
R_2 = 2
H = 2.123

n = 1000

t=0
dt = 0.01

indc = 0 #Indica si se ha pasado por el 0

#Sacado de la tarea 2
def Simpson2D(x_i, x_f, n, funcion, y):
    delta_x = (x_f-x_i)/n
    i = 0
    terminoSimp = 0
    for i in range(n//2+1):
        terminoSimp += funcion(x_i+2*(i-1)*delta_x,y) + 4*funcion(x_i+(2*i-1)*delta_x,y) + funcion(x_i+2*i*delta_x,y)
    return terminoSimp*(delta_x/3)

def integrante(x,y):
    return -y/(((y**2)+(x**2))**(3/2))

def analitica(x,y):
    return -x/(y*(((x**2)+y(y**2))**(1/2)))
    

#Integral numerica#: Usar Simpson2D con un y fijo e intervalo R_1 y R_2

#Pasos integrales#: Con un y fijo, calcular el Simpson con un n dado y comparar con la analitica, si es 
#la resta es mayor a cierto crietrio, se repite el proceso para un n mas grande, hasta que la resta sea
#lo suficientemente pequeña.


#RK4

def F(y,t):
    return np.array([y[1],Simpson2D(R_1,R_2,n,integrante,y[0])])
  
def Analitica(y):
    return R_2/(y*(np.sqrt(R_2**2+y**2))) - R_1/(y*(np.sqrt(R_1**2+y**2)))
         
#Y inicial#
y = np.array([H,0])        

SolP = [H]
SolV = [0]
T = [0]  
DIFF = []
posf = 0
timef = 0
while indc == 0:
    k1 = F(y,t)
    AN = Analitica(y[0])
    diff = AN - k1[1]
    DIFF.append(diff)
    print(k1)
    k2 = F(y+(dt/2)*k1,t+dt/2)
    k3 = F(y+(dt/2)*k2,t+dt/2)
    k4 = F(y+dt*k3,t+dt)
    Y = y +(1/6)*(k1+2*k2+2*k3+k4)*dt
    SolP.append(Y[0])
    
    SolV.append(Y[1])
   
    y = Y
    if t >90:
        posf = Y[0]
        timef = t
        indc = 1
    t = t + dt
    T.append(t+dt)

fig, ax = plt.subplots(1,1,figsize=(15,12))
plt.plot(T, SolP, color="crimson",label="data")
ax.grid(True, linestyle="--",color="dimgray")
ax.tick_params(axis='both', which='major', labelsize=14)
ax.tick_params(axis='both', which='minor', labelsize=14)
plt.xlabel('Tiempo ',fontsize=20)
plt.ylabel('Altura ',fontsize=20)
plt.title('Movimiento Armónico',fontsize=22)
plt.show()

fig, ax = plt.subplots(1,1,figsize=(15,12))
plt.plot(SolP, SolV, color="crimson",label="data")
ax.grid(True, linestyle="--",color="dimgray")
ax.tick_params(axis='both', which='major', labelsize=14)
ax.tick_params(axis='both', which='minor', labelsize=14)
plt.xlabel('Altura',fontsize=20)
plt.ylabel('Velocidad',fontsize=20)
plt.title('Posición vs Velocidad',fontsize=22)
plt.show()


DIFF2 = []
y = np.array([H,0])  
for k in np.arange(10,100000,1000):
    n = k
    SS = Simpson2D(R_1,R_2,n,integrante,y[0])
    AN = Analitica(y[0])
    diff = AN-SS
    DIFF2.append(diff)
    
 
fig, ax = plt.subplots(1,1,figsize=(15,12))
plt.plot((np.arange(10,100000,1000)),(DIFF2), color="crimson",label="data")

plt.xscale("log")
ax.grid(True, linestyle="--",color="dimgray")
ax.tick_params(axis='both', which='major', labelsize=14)
ax.tick_params(axis='both', which='minor', labelsize=14)
plt.xlabel('N',fontsize=20)
plt.ylabel('Error',fontsize=20)
plt.title('Convergencia',fontsize=22)
plt.show()
    






