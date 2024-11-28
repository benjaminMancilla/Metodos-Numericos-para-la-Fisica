# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 12:33:36 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Definimos el metodo de integracion, este es la regla de Simpson implementado en la Tarea 2
def Simpson(x_i, x_f, n, funcion):
    delta_x = (x_f-x_i)/n
    i = 0
    terminoSimp = 0
    for i in range(n//2+1):
        terminoSimp += funcion(x_i+2*(i-1)*delta_x) + 4*funcion(x_i+(2*i-1)*delta_x) + funcion(x_i+2*i*delta_x)
    return terminoSimp*(delta_x/3)
#Luego definimos el integrando
def funcion(x):
    return x*np.sin(1/x)

#Haremos esto de dos formas, la idea es probar cual es la mas integra con la logica del problema.
#La primera es dejar un epsilon fijo, lo haremos bastante pequeño para llegar a valores cercanos al error 
#de la maquina. 
epsiloN = 1*(10**(-15)) #El limite es de exponente -15, si hacemos el epsilon aun mas pequeño la maquina lo considerara como un 0.
n=1000000 #Nos aseguramos con un n bastante grande
I1=Simpson(-2, -1*epsiloN, n, funcion) #Integral desde -2 hasta epsilon
I2=Simpson(epsiloN, 2, n, funcion) #Integral desde 2 hasta epsilon
I3 = I1+I2 #La integral total es simplemente la suma
print("El valor de la integral es " + str(I3) + ".") 

#Se nos pide graficar como converge el valor de la integral a medida que aumenta n, osea graficamos
# un resultado por cada n. Para visualisar mejor el resultado le restamos el valor de la integral con 
#n muy grande.

N = np.arange(100,1000,2).tolist() #Definimos los N #SOLO NUMEROS PARES (asi funciona Simpson)
Integralesl = []
Integrales = []
Nlog = []
for n in N: #Calculamos la integral para cada n
    I1 = Simpson(-2,-epsiloN,n, funcion)
    I2 = Simpson(epsiloN,2,n, funcion)
    Integralesl.append(np.log(abs(I1+I2)))
    Integrales.append(I1+I2)
    Nlog.append(np.log(n))
    
#Graficamos


deN = pd.DataFrame({"Integrales":Integrales})
deNx = deN.set_axis(N, axis='index')

fig, ax = plt.subplots(figsize=(10,8))
plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey
ax.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background

colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41', # matrix green
]
deNx.plot( ax=ax, color=colors)

n_lines = 10
diff_linewidth = 1.05
alpha_value = 0.03
for n in range(1, n_lines+1):
    deNx.plot(
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)


ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
ax.set(xlabel='n', ylabel='Integral', title='Convergencia')

plt.show()

#Hacemos lo mismo pero con un epsilon dependiente del n

#Integrales = []
#for n in N: #Calculamos la integral para cada n
#    epsilon = 4/n #el valor de epsilon depende de la "anchura" de la particion, el 4 es simplemente por 2-(-2)
#    I1 = Simpson(-2,-epsilon,n, funcion)
#    I2 = Simpson(epsilon,2,n, funcion)
#    Integrales.append(np.log(abs((I1+I2)-I3)))

#Grafico la funcion simplemente para visualizar
Y = []
N1 = np.linspace(-0.1,0.1,1000)
for x in N1:
    if x == 0:
        Y.append(0)
    else:
        Y.append(funcion(x))

dynX = pd.DataFrame({"Funcion":Y})       
 
dyN = dynX.set_axis(N1, axis='index')

fig, ax = plt.subplots(figsize=(12,8))
plt.style.use("seaborn-dark")
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey
ax.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background

colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41', # matrix green
]
dyN.plot( ax=ax, color=colors)

n_lines = 10
diff_linewidth = 1.05
alpha_value = 0.03
for n in range(1, n_lines+1):
    dyN.plot(
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)


ax.grid(color='#2A3459')
ax.set_xlim([-0.005, 0.005])
ax.set_ylim([-0.25, 0.25])  # to not have the markers cut off
ax.set(xlabel='x', ylabel='F(x)', title='Funcion')

plt.show()
        



    