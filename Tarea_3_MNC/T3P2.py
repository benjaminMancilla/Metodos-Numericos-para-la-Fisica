# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:59:42 2022

@author: benja
"""
import numpy as np


#Se nos pide resolver una ecuacion por metodo de Newton
#Como se nos dice en el hint la funcion varia de alpha, por lo que derivaremos a partir de esa variable
#Primero debemos definir las constantes, es decir los limites de integracion y el n
x_i = 0
x_f = 1
n = 10**6
h = 1/n
epsilon = 1*(10**(-14))


#Luego definimos el integrando, en este caso dos variables, pero en realidad la que vamos a variar es a.
#Ademas agregamos el -1/2 para tener lista nuestra funcion a evaluar
def funcion(x,a):
    return ((1+a*(x**1.5))**(-1)) - 0.5

#Es igual que el simpson de siempre pero con la varible a (alpha)
def SimpsonS(a):
    delta_x = (x_f-x_i)/n
    i = 0
    terminoSimp = 0
    for i in range(n//2+1):
        if i == 0: #Lo malo de esta forma para calcular la integral es que para el primer termino, los valores de x no son del todo preciso, para este caso genera problemas incluso, ya que nuestro x inicial es 0 y se forma un numero complejo.
            terminoSimp += funcion(x_i,a) + 4*funcion(x_i,a) + funcion(x_i+2*i*delta_x,a)     
        else:         
            terminoSimp += funcion(x_i+2*(i-1)*delta_x,a) + 4*funcion(x_i+(2*i-1)*delta_x,a) + funcion(x_i+2*i*delta_x,a)
    return terminoSimp*(delta_x/3)


#Ahora que ya tenemos nuestra f(a), solo falta aplicar el metodo

#Para evitar problemas de escritura engorrosa con los parametros, dejamos f fijo


#Nos falta definir la derivada, la cual se define con a variable
def derivada(a):
    return (SimpsonS(a+h)-SimpsonS(a-h))/(2*h)


#Definimos el metodo, n es el termino n y n_1 es el termino n+1, la iteracion se repite hasta que exista
#una diferencia minima entre el termino anterior y el nuevo, eso significa que estamos oscilando
#alrededor de la raiz, lo cual nos indica que estamos muy cerca de la solucion.
def Newton(fx,fd,x0):
    n = x0
    n_1 = n - fx(n)/fd(n)
    while abs(n_1-n)>epsilon:
        n = n_1
        n_1 = n - fx(n)/fd(n)
    return n_1

d = Newton(SimpsonS,derivada,3)

print("La solucion es x=" + str(d) + ".")



