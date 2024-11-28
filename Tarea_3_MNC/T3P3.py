# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 00:58:34 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.integrate as sc

#Se nos pide trabajar con una funcion que no conocemos pero si su inversa
#Por definicion, sabemos que esta funcion debe retornar el valor "y" que cumpla x = y*(e**y), ya que
#sabemos que x*(e**x) es la inversa.
#Por lo tanto nuestra funcion no es nada mas que despejar una ecuacion, es decir, una solucion no lineal
#Para resolver esta ecuacion, y por ende, definir nuestra funcion usaremos un metodo mostrado en clases
#todavia por definir, dependiendo de la naturaleza de la funcion es si podemos utilizar Newton

#Usamos Newton con un epsilon pequeño
epsilon = 1*(10**(-14))
h = 1/(10**6)
def Newton(fx,fd,x0,x_i):
    n = x0
    n_1 = n - fx(n,x_i)/fd(n,x_i)
    while abs(n_1-n)>epsilon:
        n = n_1
        n_1 = n - fx(n,x_i)/fd(n,x_i)
    return n_1

#Definimos nuestro intervalo
X = np.linspace(0,10,61)

def eccW(y,x_i): #y es la variable que buscara la raiz,es decir la variable auxiliar, y x_i es la variable real.
    return y*(np.e**y)-x_i#el menos es para que Newton pueda buscar la raices (igualar a 0)

def deccW(y,x_i): #derivada central
    return (eccW(y+h,x_i)-eccW(y-h,x_i))/(2*h)
    
#Calculamos valores de la funcion, es decir, las raices para nuestra ecuaciones.
#El valor y0 se estima gracias a Wolfram, se evaluan desde 0 hasta 10 y se saca un promedio al ojo
y0=1.2
def W(x): #Ya con la derivada, la funcion y le metodo listo, juntamos todo dentro de una funcion, la cual solo depende de x, esto nos sera util para integrarla mas adelante
    raiz = Newton(eccW,deccW,y0,x)
    return raiz
    
Wa = []
for x in X:
    raiz = W(x)
    Wa.append(raiz)


#Graficamos
dfN = pd.DataFrame({"Newton":Wa})
dfNx = dfN.set_axis(X, axis='index')

fig, ax = plt.subplots(figsize=(10,10))
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
dfNx.plot( ax=ax, color=colors)

n_lines = 10
diff_linewidth = 1.05
alpha_value = 0.03
for n in range(1, n_lines+1):
    dfNx.plot(
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)
    
for column, color in zip(dfNx, colors):
    ax.fill_between(x=dfNx.index,
                    y1=dfNx[column].values,
                    y2=[0] * len(dfNx),
                    color="#FE53BB",
                    alpha=0.1)

ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
ax.set(xlabel='x', ylabel='Raiz', title='Raices')

plt.show()

#Para la parte b hay que integrar numericamente W
x_1 = 0
x_f = 10
n = 10**6
#Simspon no me funcionaba asi que use Trapecios           
def Trapecio(x_1, x_f, n, funcion):
    delta_x = (x_f-x_1)/n
    i = 0
    terminoTrap = 0
    for i in range(n+1):
        if (i == 0) or (i == n+1):
            terminoTrap += funcion(x_1+(i-1)*delta_x)
            i = i+1
        else:
            terminoTrap += 2 * (funcion(x_1+(i-1)*delta_x))
            
            i = i+1
            
    
    return (delta_x/2)*(terminoTrap)

#Integramos W desde 0 hasta 10
l = Trapecio(x_1,x_f,n,W)

#Luego analiticamente
m = 0
borde = [10**-30,10] #Tengo que tender un limite ya que hay divison por 0
for x in borde:
    raiz = Newton(eccW,deccW,y0,x) #por teo del calculo la integral en este caso es solo la expresion del enunciado evaluado en 10 menos evaluado en el limite tendiendo a 0
    if x == borde[0]:    
        m -= x*((raiz) - 1 + (1/raiz))
    else:
        m += x*((raiz) - 1 + (1/raiz))
        

print("La integral numerica entrega el valor " + str(l) + ".")
print("La integral analitica entrega el valor " + str(m) + ".")
xd = l-m

        