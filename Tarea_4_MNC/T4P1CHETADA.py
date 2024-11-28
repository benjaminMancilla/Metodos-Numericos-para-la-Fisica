# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:38:02 2022

@author: benja
"""
import autograd.numpy as np
import autograd as ad
from autograd import grad, jacobian
import matplotlib.pyplot as plt
from scipy.integrate import quad
#Defino las funciones para evaluar mas tarde
def f1(x,y,T):
    return np.log((3*y-1)/(3*x-1))+(9/(4*T))*((1/y)-(1/x))-(1/(3*y-1))+(1/(3*x-1))
def f2(x,y,T): 
    return (8*T/3)*((1/(3*y-1))-(1/(3*x-1)))-(1/(y**2))+(1/(x**2))
def p(v,T):
    return (8*T)/(3*v-1) - 3/(v**2)

#Arreglo de temperaturas
t = np.arange(0.99,0.85,-0.01)
sol = [] #Igual a la de abajo pero sin la prediccion oficial (lista de resultados)
c = [np.array([1.2,0.8])] #Esta lista es la que contiene los "Ansatz" de los valores iniciales
print("TEST")
for item in t: #Una par de raices por cada T 
    T = item #Defino T para puedan operar las funciones
    #Defino a x como variable, x[0] es vg y x[1] es vl
    fn1 = lambda x: np.log((3*x[0]-1)/(3*x[1]-1))+(9/(4*T))*((1/x[0])-(1/x[1]))-(1/(3*x[0]-1))+(1/(3*x[1]-1))
    fn2 = lambda x: (8*T/3)*((1/(3*x[0]-1))-(1/(3*x[1]-1)))-(1/(x[0]**2))+(1/(x[1]**2)) 
    #Calculo el Jacobiano con autoGrad
    #Esta funcion crea una clase que entrega una funcion si es que se le da un parametro
    #En este caso tiene que ser un array de 2*1
    jac1 = jacobian(fn1) 
    jac2 = jacobian(fn2)


    i = 0 #Antes lo use como controlador de iteraciones pero lo saque porque no era necesario
    e = 0.0000000000001 #Epsilon pequeño
    M = 2 #Dimension de los F(x0)
    N = 2 #Dimension de los x0
    limit = 100000 #Limite de iteraciones (no se usa)
    error = 1000000 #Esto es solo para darle un valor inicial al error, mientras sea mayor que e todo bien
    x0 = np.array([c[len(c)-1][0],c[len(c)-1][1]]).reshape(N,1) #Defino la tupla y le doy la forma de columna con reshape
    while np.any(abs(error)>e): #While que maneja el newton
    
        primero = np.array([fn1(x0),fn2(x0)]).reshape(M,1)#Primer valor son las funciones anteriores evaluadas en x0
        flatx0 = x0.flatten() #Aveces las matrices del tipo N*1 no funcionan bien en jacobian, por la documentacion
        #use este operador ya que se recomendaba fuertemente su uso. Este solo transforma cualquier matriz en una de 1 dim
        jac = np.array([jac1(flatx0),jac2(flatx0)]) #Junto los jac de cada dimension
        jac = jac.reshape(N,M) #Le doy la forma cuadrada al jac tomando el jac 2 y poniendolo debajo del 1 (descrip grafica)
        n_1 = x0 - np.linalg.inv(jac)@primero #Paso newtoniano, linalg.inv invierte la matriz y @ es el producto punto
        error = n_1-x0 #Veo si me muevo poco
        x0 = n_1 #Paso iterativo siguiente
        i += 1 #Sumo una iteracion (No se usa)
    #Se rompe el ciclo, n_1 es raiz
    #Se agrega a ambas listas ya dichas
    sol.append(n_1)
    c.append(n_1)
    #Se printean las funciones sobre las raices para asegurar que estas den 0 (o un num cercano)
    print(f1(n_1[0][0],n_1[1][0],item))
    print(f2(n_1[0][0],n_1[1][0],item))
    #Se calcula la integral de Maxwell para asegurarse 2 veces, esta tiene que ser 0 tambien
    I = quad(p, n_1[1][0], n_1[1][0], args=(T))
    print(I)
 
#Se acaba el for, todas las raices calculadas
#Separo raiz por cada v
VG = []
VL = []
for s in sol:
    VG.append(s[0][0])
    VL.append(s[1][0])

#Ploteo
fig, ax = plt.subplots()
ax.plot(t, VG, label = "v_g")
ax.plot(t, VL, label = "v_l")
plt.xlabel('Temperatura')
plt.ylabel('Volumen')
plt.legend()


ax.set_title('v vs T')

    

    
        
    