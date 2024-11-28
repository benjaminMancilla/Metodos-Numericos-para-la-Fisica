# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:18:01 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt

#P2#
#Conocemos la formula para calcular el voltaje, o potencial electrico, y a la vez se sabe
#la posicion y la carga de cada una de las particulas (cargas) en el tablero.
#Con esto datos se buscara definir una sola funcion que necesite una posicion (x,y), es decir
#la posicion que queremos medir, y una lista que contenga la posicion y la carga de los puntos
#del tablero, esta funcion entregara un vector, que sera el campo electrico en la componente
#x e y. Para esto ultimo deberemos definir 3 whiles, uno para x (osea x+h y x-h) otro para
#h y finalmente uno para y (osea y+h y y-h).

#Primer paso seria crear la lista de las cargas, ya que sin esta no podemos resolver este probema
#Una propiedad que tiene la funcion E es que no necesariamente funciona solo con la distribucion
#del tablero, sino que con cualquier distribucion, siempre y cuando se ingrese una lista en el
#input

tableC = []
indg = 0
indx = 0.75
indy = 0.75
indca = 10

while indg < 25:
    tableC.append([indx, indy, indca]) 
    indg = indg + 1
    indca = indca*(-1)
    
    if indx == 6.75:
        
        indx = 0.75
        indy = indy + 1.5
        
        
        
    else: indx = indx + 1.5   
    
#Una vez que tenemos nuetra lista, hay que definir la funcion E
#Lo primero antes es que hay que definir una funcion auxiliar que calcule el voltaje
#total en un punto, es decir, a partir de un x,y e una lista, te calcula la suma total
#de los potenciales de cada carga individual.

#NOTA: no es necesario crear esta funcion, pero sin ella la funcion E quedaria exageradamente
#larga (5 for dentro de la funcion).

#Resumen de U: toma cada carga y calcula el modulo con respecto a x,y, luego hace la divison
# y agrega el resultado a la lista para despues sumar todo y obtener el V total, en el caso
# de que el modulo sea 0 (es decir que se esta calculando el voltaje que siente una carga),
#simplemente se dice que ese voltaje en especifico es 0 (ya que es si misma)


def U(cargas, x, y):
    
    Voltajes = []
    for carga in cargas:
        q = carga[2]
        d = np.sqrt(((x-carga[0])**2)+((y-carga[1])**2))   
        if d == 0:
            v = 0.0000001 #no pongo 0 para que no se indefina en el log que calcular el color, pero teoricamente es 0
            Voltajes.append(v)
            
        else:
            v = q/d
            Voltajes.append(v)    
        
                     
    return Voltajes        
    
        
        

def E(cargas, x, y):
    h=0.01
    V_xplush_y= U(cargas,x+h,y)
    V_xminush_y= U(cargas,x-h,y)
    V_x_yplush= U(cargas,x,y+h)
    V_x_yminush= U(cargas,x,y-h)
    V_x_y= U(cargas,x,y)
    
    Ex = []
    Ey = []
    i=0
    while i < len(cargas):
        derivParcialX = (-1)*((V_xplush_y[i] - V_xminush_y[i])/(2*h))
        derivParcialY = (-1)*((V_x_yplush[i] - V_x_yminush[i])/(2*h))
        Ex.append(derivParcialX)
        Ey.append(derivParcialY)
        i+=1
        
    #Superposicion
    
    return [sum(Ex),sum(Ey)]

#Grafico COLOR

x = np.arange(0, 7.5, 0.05).tolist()
y = np.arange(0, 7.5, 0.05).tolist()
colors = []

def CampoColor(cargas,x,y):
    Ejex = []
    Ejey = []
    Color = []
    for posx in x:
        for posy in y:
            Ejex.append(posx)
            Ejey.append(posy)
            CampE = E(cargas,posx,posy)
            modulo = np.sqrt((CampE[0])**2+(CampE[1])**2)
            Color.append(modulo)
    
    return [Ejex, Ejey, Color]

InfoC = CampoColor(tableC,x,y)
XC = InfoC[0]
YC = InfoC[1]
Colores = InfoC[2]        
plt.scatter(XC,YC, s=1, c=Colores)
cbar = plt.colorbar(extend="both")
plt.clim(0,300)
plt.axis("scaled")
plt.figure(figsize=(8,8))
cbar.set_label(label="Gradiente", size=12)
plt.title("Campo electrico")


#Grafico STREAM

def CampoStream(cargas,x,y):
    MatrizX = []
    MatrizY = []
    for posy in y:
        lote = []
        for posx in x:
            CampE = E(cargas,posx,posy)
            lote.append(CampE[0])
            
        MatrizX.append(lote)
    
    for posx in x:
        lote = []
        for posy in y:
            CampE = E(cargas,posx,posy)
            lote.append(CampE[1])
            
        MatrizY.append(lote)
            
    MatriX = np.array(MatrizX)
    MatriY_ = np.array(MatrizY)
    MatriY = MatriY_.transpose()
    
    
    return [MatriX, MatriY]
XX = np.arange(0, 7.5, 0.05)
YY = np.arange(0, 7.5, 0.05)


plt.streamplot(XX, YY, CampoStream(tableC,x,y)[0], CampoStream(tableC,x,y)[1], linewidth=1, cmap=plt.cm.cool,density=2, arrowstyle='->', arrowsize=0.7)





    
    

