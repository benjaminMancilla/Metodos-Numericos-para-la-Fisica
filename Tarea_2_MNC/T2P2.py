# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:45:30 2022

@author: benja
"""
#P2#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Simpson(x_i, x_f, n, funcion):
    delta_x = (x_f-x_i)/n
    i = 0
    terminoSimp = 0
    for i in range(n//2+1):
        terminoSimp += funcion(x_i+2*(i-1)*delta_x) + 4*funcion(x_i+(2*i-1)*delta_x) + funcion(x_i+2*i*delta_x)
    return terminoSimp*(delta_x/3)
   
        

    
def Trapecio(x_i, x_f, n, funcion):
    delta_x = (x_f-x_i)/n
    i = 0
    terminoTrap = 0
    for i in range(n+1):
        if (i == 0) or (i == n+1):
            terminoTrap += funcion(x_i+(i-1)*delta_x)
            i = i+1
        else:
            terminoTrap += 2 * (funcion(x_i+(i-1)*delta_x))
            
            i = i+1
            
    
    return (delta_x/2)*(terminoTrap)
    


def MidPoint(x_i, x_f, n, funcion):
    delta_x = (x_f-x_i)/n
    i = 0
    midpoints = 0
    while i < n:
        c = x_i + (i - 0.5)*delta_x
        C = funcion(c)
        midpoints += C
        i = i+1
         
    return delta_x*midpoints
    
           
        
    

def funcion(x):
    return x*np.exp(x)*np.sin(x)

def analitica(x_i, x_f):
    final = ((1/2)*(np.exp(x_f)))*(np.cos(x_f)-x_f*np.cos(x_f)+x_f*np.sin(x_f))
    inicial = ((1/2)*(np.exp(x_i)))*(np.cos(x_i)-x_i*np.cos(x_i)+x_i*np.sin(x_i))
    return final-inicial

x_i = 0
x_f = (3/5)*np.pi
N = np.arange(20,100,2).tolist()
N_1 = np.arange(20,98,2).tolist()
#Creo las listas para n de cada metodo
datosSimp = []
datosTrap = []
datosMid = []

SvsS = []
TvsT = []
MvsM = []

SA = []
TA = []
MA = []

fx = analitica(x_i,x_f)

for n in N:
    S = Simpson(x_i, x_f, n, funcion)
    T = Trapecio(x_i, x_f, n, funcion)
    M = MidPoint(x_i, x_f, n, funcion)
    datosSimp.append(S)
    datosTrap.append(T)
    datosMid.append(M)
    
i = 0
#Diferencia entre Simp y Simp
while i+1 < len(N):
    m = (abs((datosSimp[i] - datosSimp[i+1])))
    SvsS.append(m)
    i += 1

i = 0
#Diferencia entre Trap y Trap
while i+1 < len(N):
    m = (abs((datosTrap[i] - datosTrap[i+1])))
    TvsT.append(m)
    i += 1
  
i = 0
#Diferencia entre Mid y Mid
while i+1 < len(N):
    m = (abs((datosMid[i] - datosMid[i+1])))
    MvsM.append(m)
    i += 1

i = 0
#Diferencia entre Simp,Trap,Mid y Analitca
#Puedo usar el logaritmo de la suma y el ejex queda como los log(n), probar para ver si
#queda como los del profe
while i < len(N):
    ms = (abs(-datosSimp[i] + fx))
    mt = (abs(-datosTrap[i] + fx))
    mm = (abs(-datosMid[i] + fx))
    SA.append(ms)
    TA.append(mt)
    MA.append(mm)
    i += 1


#El plot lo saque de una pagina de internet, realmente es bonito asi que no me pude resistir

df = pd.DataFrame({"Simp":SA,"Trap":TA,"Mid":MA})
dp = pd.DataFrame({"Simp":SvsS,"Trap":TvsT,"Mid":MvsM})

fig, ax = plt.subplots()
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
df.plot( ax=ax, color=colors)

n_lines = 10
diff_linewidth = 1.05
alpha_value = 0.03
for n in range(1, n_lines+1):
    df.plot(
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)


ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
ax.set_ylim(0)
ax.set(xlabel='n', ylabel='Diferencia', title='Error')

plt.show()

    
fig, ax = plt.subplots()
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
dp.plot( ax=ax, color=colors)

n_lines = 10
diff_linewidth = 1.05
alpha_value = 0.03
for n in range(1, n_lines+1):
    dp.plot(
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)


ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
ax.set_ylim(0)

ax.set(xlabel='n', ylabel='Diferencia', title='Convergencia')

plt.show()







Nlog_1 = []
Nlog = []
SAlog = []
TAlog = []
MAlog = []
SSlog = []
TTlog = []
MMlog = []
for n in N_1:
    Nlog_1.append(np.log(n))
for n in N:
    Nlog.append(np.log(n))   
for n in SA:
    SAlog.append(np.log(n))
for n in TA:
    TAlog.append(np.log(n))
for n in MA:
    MAlog.append(np.log(n))
for n in SvsS:
    SSlog.append(np.log(n))
for n in TvsT:
    TTlog.append(np.log(n))
for n in MvsM:
    MMlog.append(np.log(n))


dfN = pd.DataFrame({"Simp":SAlog,"Trap":TAlog,"Mid":MAlog})
dpN = pd.DataFrame({"Simp":SSlog,"Trap":TTlog,"Mid":MMlog})
dfNx = dfN.set_axis(Nlog, axis='index')
dpNx = dpN.set_axis(Nlog_1, axis='index')

fig, ax = plt.subplots()
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


ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
ax.set(xlabel='log(n)', ylabel='Diferencia', title='Error log')

plt.show()


fig, ax = plt.subplots()
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
dpNx.plot( ax=ax, color=colors)

n_lines = 10
diff_linewidth = 1.05
alpha_value = 0.03
for n in range(1, n_lines+1):
    dpNx.plot(
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)


ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])
ax.set(xlabel='log(n)', ylabel='Diferencia', title='Convergencia log')

plt.show()






    



    