# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:07:02 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

#Defino la funcion y sus derivadas
def T(x,x1,x2,y1,y2,v1,v2):
    return ((np.sqrt((x**2)+(y1**2)))/v1) + ((np.sqrt(((x2-x1-x)**2)+(y2**2)))/v2)

def dT(x,x1,x2,y1,y2,v1,v2):
    return (x/(v1*np.sqrt((x**2)+(y1**2)))) + ((-x2+x1+x)/(v2*np.sqrt(((-x2+x1+x)**2)+(y2**2))))

def ddT(x,x1,x2,y1,y2,v1,v2):
    return ((y1**2)/(v1*(((x**2)+(y1**2))**(3/2)))) + ((y2**2)/(v2*((((x1-x2+x)**2)+(y2**2))**(3/2))))

#Defino las ctes
x1 = -3
y1 = 2
x2 = 1.5
y2 = -1.8
n1 = 1.05
n2 = 1.35
c = 1 
v1 = c/n1
v2 = c/n2
epsilon= 10**-8

#Limite 4.5 porque este numero significa que la luz se torna en 90 grados, lo cual es lo maximo fisicamente

#Ploteo la funcion y sus derivadas
X = np.linspace(0,4.5,100)
fig, ax = plt.subplots()
ax.plot(X, T(X,x1,x2,y1,y2,v1,v2), label = "t(x)")
plt.xlabel('Distancia x')
plt.ylabel('Tiempo t')
plt.legend()
ax.set_title("Derivada orden 0")
plt.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(X, dT(X,x1,x2,y1,y2,v1,v2), label = "dt(x)")
plt.xlabel('Distancia x')
plt.ylabel('Tiempo t')
plt.legend()
ax.set_title("Derivada orden 1")
plt.legend()
plt.show()

fig, ax = plt.subplots()
ax.plot(X, ddT(X,x1,x2,y1,y2,v1,v2), label = "d(dt(x))")
plt.xlabel('Distancia x')
plt.ylabel('Tiempo t')
plt.legend()
ax.set_title("Derivada orden 2")
plt.legend()
plt.show()
#Como la funcion diverge despues de 4.5 (x2-x1) no tiene sentido pensar en un minimo en un intervalo mayor
#Como solo se tiene un minimo, se puede usar newton.

#Introduzco Newton
def Newton(fx,fd,x0,x1,x2,y1,y2,v1,v2):
    n = x0
    n_1 = n - fx(n,x1,x2,y1,y2,v1,v2)/fd(n,x1,x2,y1,y2,v1,v2)
    while abs(n_1-n)>epsilon:
        n = n_1
        n_1 = n - fx(n,x1,x2,y1,y2,v1,v2)/fd(n,x1,x2,y1,y2,v1,v2)
    return n_1

#Calculo el x minimo por medio de Newton
minimo = Newton(dT,ddT,3,x1,x2,y1,y2,v1,v2)

print("El x optimo es " + str(minimo) + ".")
print()

#La ley de snell nos dice que n1sen(theta1)-n2sen(theta2)=0
#Para que esto se cumpla x debe ser el optimo, es decir, debe ser el camino de la luz
#Lo podemos comprobar simplemente remplazando en la relacion anterior y verificando el resultado
xp = minimo
snell = n1*(xp/np.sqrt(xp**2 + y1**2)) - n2*((x2-x1-xp)/np.sqrt((x2-x1-xp)**2 + y2**2))
print("Este x evaluado en la ley de snell nos entrega que la resta de ambos terminos es " + str(snell) + ".")

X1 = np.linspace(-6,-2,100)


sin1 = []
sin2 = []

for item in X1:
    o = Newton(dT,ddT,3,item,x2,y1,y2,v1,v2)
    theta1 = (o/np.sqrt(o**2 + y1**2))
    theta2 = ((x2-item-o)/np.sqrt((x2-item-o)**2 + y2**2))
    sin1.append(theta1)
    sin2.append(theta2)


fig, ax = plt.subplots()
ax.plot(sin1, sin2, label = "n2/n1")
plt.xlabel('sen(theta1)')
plt.ylabel('sen(theta2)')
plt.legend()
ax.set_title("Sen1/Sen2")
plt.legend()
plt.show()

#Calculo la pendiente
slope = linregress(sin1,sin2)[0]

print("La pendiente del grafico es " + str(slope) + ", mientras que n1/n2 es " + str(n1/n2) + "." )

    
    

