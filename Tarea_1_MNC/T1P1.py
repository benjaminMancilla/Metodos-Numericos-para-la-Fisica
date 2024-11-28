#PREGUNTA 1#
"""
Created on Wed Mar 23 09:16:07 2022

@author: benja
"""

import math
import numpy as np

#P1#
#Nota: dicc con llave para cada antena, corresponden 3 datos por cada una, cada uno de estos representa el angulo en grados detectado en el tiempo

datosp1 = {"alpha": [[9,54.80],[10,54.06],[11,53.34]], "beta": [[9,65.59],[10,64.90],[11,63.62]]} 

#como los datos estan en grados y math usa radianes, creo funcion simple entre unidades

def grad(ang):
    return ((ang)/180)*math.pi


#ang1 es alpha y ang2 es beta, dist es simplemente "a"

def posY(ang1,ang2,dist):
    a1 = grad(ang1)
    a2 = grad(ang2)
    resta = a2 - a1
    return ((math.sin(a1))*(math.sin(a2))*dist)/(math.sin(resta))

#geometricamente se forman 2 triangulos, entregando 2 formas de cacular x e y
#en y no existe diferencia en el resultado, en x si, debido al origen de coord y a la 
#dispocision geometrica del problema, sin embargo, a pesar de que la expresion sea distinta
#el resultado al menos numericamente deberia ser el mismo

def posX1(ang1,ang2,dist):
    a1 = grad(ang1)
    a2 = grad(ang2)
    resta = a2 - a1
    return ((math.cos(a1))*(math.sin(a2))*dist)/(math.sin(resta))

def posX2(ang1,ang2,dist):
    a1 = grad(ang1)
    a2 = grad(ang2)
    resta = a2 - a1
    return (((math.cos(a2))*(math.sin(a1))*(dist))/(math.sin(resta))) + dist


def derivada_central1(funcion, h, dicc, dist):
    
    #crear una forma de traspasar los segundos a angulos, probablemente usando
    #los segundos como claves para buscar en la lista del principio, luego se toma el angulo
    #y se agrega al array
    
    datosalpha = dicc["alpha"]
    ialpha = []
    
    for tupla in datosalpha:
        ang = tupla[1]
        ialpha.insert(0, ang)
        
    datosbeta = dicc["beta"]
    ibeta = []
    
    for tupla in datosbeta:
        ang = tupla[1]
        ibeta.insert(0, ang)
        
    sumah = 1 + h
    restah = 1 - h 
    
              
        
    return (funcion(ialpha[sumah],ibeta[sumah],dist)-(funcion(ialpha[restah],ibeta[restah],dist))) / (2*h)

#Con esta funcion podemos calcular la velocidad para cada uno de los componentes
#Para calcular el total de la velocidad podemos usar el modulo de ambos de estos 
#para obtener la rapidez y luego usar el angulo para tener a velocidad en polares

def rapidez(vx,vy):
    return np.sqrt(vx**2 + vy**2)

def angulo(vx,vy):
    return math.atan(vy/vx)

def derivada_central2(funcion, h, dicc, dist):
    datosalpha = dicc["alpha"]
    ialpha = []
    
    for tupla in datosalpha:
        ang = tupla[1]
        ialpha.insert(0, ang)
        
    datosbeta = dicc["beta"]
    ibeta = []
    
    for tupla in datosbeta:
        ang = tupla[1]
        ibeta.insert(0, ang)
        
    sumah = 1 + h
    restah = 1 - h 
    
              
        
    
    return (funcion(ialpha[sumah],ibeta[sumah],dist) + funcion(ialpha[restah],ibeta[restah],dist) - 2*funcion(ialpha[1],ibeta[1],dist))/h**2

Vx = derivada_central1(posX1, 1, datosp1, 500)
Vy = derivada_central1(posY, 1, datosp1, 500)

velocidad = [rapidez(Vx,Vy),angulo(Vx,Vy)]



acx = derivada_central2(posX1, 1, datosp1, 500)
acy = derivada_central2(posY, 1, datosp1, 500)    

aceleracion = [rapidez(acx,acy),angulo(acx,acy)]

print("La velocidad tiene un modulo " + str(velocidad[0]) + " metros por segundos, y un angulo " + str(velocidad[1]) + " radianes con respecto a la normal en el segundo 10.")
print()
print("La aceleracion tiene un modulo " + str(aceleracion[0]) + " metros por segundos al cuadrado, y un angulo " + str(aceleracion[1]) + " radianes con respecto a la normal en el segundo 10.")