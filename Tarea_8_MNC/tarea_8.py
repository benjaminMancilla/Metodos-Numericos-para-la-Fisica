# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:05:32 2022

@author: benja
"""

#Tarea 8 Numerico

import numpy as np
import matplotlib.pyplot as plt
import time


plt.style.use('dark_background')

def Ma(n):
    M = np.zeros((n,n))
    for i in range(n):
        if i+1==n:
            M[i-1,i]=1
        elif i-1==-1:
            M[i+1,i] = 1
        else:
            M[i+1,i] = 1
            M[i-1,i] = 1
        M[i,i] = -2
    M[0,n-1] = 1
    M[n-1,0] = 1
    return M


Tiempos=[]
Dim =[]
t = 0
temp = 0
N = 2 
while t < 30:
    print(N)
    m = Ma(N)
    start = time.time()
    np.linalg.eig((m))
    end = time.time()
    t = end-start
    temp += t
    Tiempos.append(t)
    Dim.append(N)
    N += 1
    


fig, ax = plt.subplots(1,1,figsize=(15,12))
plt.plot(Dim, Tiempos, color="crimson",label="data",linestyle='-')
ax.grid(True, linestyle="--",color="dimgray")
ax.tick_params(axis='both', which='major', labelsize=14)
ax.tick_params(axis='both', which='minor', labelsize=14)
plt.xlabel("N",fontsize=20)
plt.ylabel('Tiempo[s]',fontsize=20)
plt.title('Tiempo de ejecución',fontsize=22)
plt.show()


#P2

#a
def Ha(a,v,N):
    H = np.zeros((N,N))
    for m in range(N):
        if m == 0:
            H[m,m+1] = 1
            H[m,m-1] = 1
            H[m,m] = 2*np.cos(2*np.pi*m*a-v)
            
            
        elif m == N-1:
            H[m,0] = 1
            H[m,N-2] = 1
            H[m,m] = 2*np.cos(2*np.pi*m*a-v)
            
        else:
            H[m,m+1] = 1
            H[m,m-1] = 1
            H[m,m] = 2*np.cos(2*np.pi*m*a-v)
            
    return H
        

#b
# alfa = 0.3
# ang = np.linspace(0,2*np.pi,5)
# listabW = list(np.zeros(5))
# listabV = list(np.zeros(5))
# for vv, i in zip(ang, range(5)):
#     W, V = np.linalg.eig(Ha(alfa,vv,100))
#     listabW[i] = W
#     listabV[i] = V
#     print(Ha(alfa,vv,100)-V)
    
#c

NN = 300 #10000
PIN = 7 #35
AA = np.linspace(0,1,NN)
# ee = np.linspace(-4, 4, NN)
ang = np.linspace(0,2*np.pi,PIN)
LISTA_EXT_A = []
LISTA_EXT_E = []

for alfa in AA:
    listab_W = list(np.zeros(PIN))
    for vv, i in zip(ang, range(PIN)):
        W, V = np.linalg.eig(Ha(alfa,vv,100))
        listab_W[i] = W
    LISTA_EXT_A.append(alfa)
    LISTA_EXT_E.append(listab_W)
        

# def find_nearest(array, value):
#     array = np.asarray(array)
#     idx = (np.abs(array - value)).argmin()
#     return array[idx]


def CampoColor(e,a):
    Ejee = []
    Ejea = []
    Color = []
    a_i = 0
    for posy in a:
        print(posy)
        for posx,i in zip(e[a_i],range(PIN)):
            color = ang[i]
            if color <= 5.23598776:
                pass
            else:
                
                for lamb in posx:
                    Ejea.append(posy)
                    # point = find_nearest(ee, lamb)
                    point =lamb
                    Ejee.append(point)
                    Color.append(color)
        a_i += 1
    
    return [Ejee, Ejea, Color]

UWU = CampoColor(LISTA_EXT_E,LISTA_EXT_A)


fig, ax = plt.subplots(1,1,figsize=(30,24))
plt.scatter(UWU[0],UWU[1], s=1, c=UWU[2], cmap="Greys_r") #RdPu"
cbar = plt.colorbar(extend="both")
plt.clim(0,2*np.pi)
cbar.set_label(label='$ \\nu $', size=24)
plt.title("Hofstadter's butterfly",size=28)
plt.show()
