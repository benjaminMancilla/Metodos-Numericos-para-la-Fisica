# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:46:49 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt

#P1#
#Primero debemos hacer el trabajo en el papel, es decir, dejar definido nuestro periodo
#con una integral dependiendo del angulo, sin que esta se indefina (para que se pueda realizar
#el calculo numerico tranquilamente)

#Esta funcion representa como nos queda lo de adentro de la integral despues del cambio
#de variable. La defino para simplificar notacion y acortar codigo

def f(theta,phi_0):
    return 4*((np.sqrt(1-(((np.sin(theta))**2)*((np.sin(phi_0/2))**2))))**(-1))
    
#Una vez hecho esto, simplemente definimos una funcion que tome un angulo inicial, un largo,
#y una cte de gravedad y aplique una integral, en este caso usaremos la regla de simpson, ya
#que no necesitamos ser tan precisos al calcular algo cte con algo que va variando dependiendo
#del angulo (T/T_0).

#Ademas agregamos la variable n para definir la presicion buscada

def Periodo(phi_0, L, g, n):
    w = np.sqrt(L/g)
    delta_phi = (np.pi/2)/n
    i = 0
    terminoSimp = 0
    #Calculo de los terminos de la regla de Simpson#
    for i in range(n//2+1):
        terminoSimp += f(2*(i-1)*delta_phi,phi_0) + 4*f((2*i-1)*delta_phi,phi_0) + f(2*i*delta_phi, phi_0)
    return terminoSimp*(delta_phi/3)*w
 




#Funcion simple para un pendulo simple 
def Periodo_0 (L, g):
    return 2*np.pi*np.sqrt(L/g)

#Ya que tenemos nuestra funciones, solo falta conseguir los datos y luego graficar

#Primero definimos las constantes para este caso, por simpleza usare una cuerda de largo 10
# y g sera igual a 10 tambien, sin embargo como estas son ctes que se repiten para T y 
#T_0 de igual el valor de estas.
L = 10
g = 10

#Luego para tener un calculo preciso usare un n = 2000, la regla de simpson da un resultando
# bastante fiable en los 1000, por lo que lo duplicare para asegurarme.

n = 1000

#Calculamos todos lo datos necesarios y definimos el intervalo para phi segun el enunciado

Rango_phi = np.arange(0, np.pi/2+np.pi/20, np.pi/20).tolist()
PeriodosT = []
for phi in Rango_phi:
    cuociente = Periodo(phi, L, g, n)/Periodo_0 (L, g)
    PeriodosT.append(cuociente)
    

#plot    
fig, ax = plt.subplots()
ax.plot(Rango_phi, PeriodosT,
        marker='o', color='b', linestyle='--', label='T/T_0')


ax.set(xlabel='Phi inicial', ylabel='T/T_0', title='Diferencia de Periodos')
ax.legend()

plt.show()
    


            
            
    
    