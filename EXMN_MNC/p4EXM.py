# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 02:30:47 2022

@author: benja
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK45, solve_ivp, odeint

#Base el codigo en uno de internet 
#chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://dspace.sunyconnect.suny.edu/bitstream/handle/1951/71154/3DmotionofCharge.pdf?sequence=1&isAllowed=y
#El paper que use fue ese
B = 1
m = 1
q = -1
pi = np.pi

v0 = 1/4

R0 = v0*m/(q*B)

f0 = abs(v0/(2*pi*R0))

T0 = 1/f0

N = 10000

t = np.linspace(0,25*T0,N)


def r(v):
    return np.linalg.norm(v)

def E(r,Rq):
    n = len(r)
    assert len(r) == len(Rq)
    mod2 = 0
    for i in range(n):
        mod2 = mod2 + (r[i] - Rq[i])**2
    if mod2 == 0:
        return 0
    mod = np.sqrt(mod2)
    aux = q/(mod) * (r-Rq)/(mod)
    return aux

def Etot(r,r1,r2,r3):
    Etot = E(r,r1)+E(r,r2)+E(r,r3)
    return Etot


r1_0 = np.array([0,1+R0,0])

r2_0 = np.array([-np.cos(pi/6),-np.sin(pi/6)+R0,0])

r3_0 = np.array([np.cos(pi/6),-np.sin(pi/6)+R0,0])

dtr1_0 = np.array([-v0,0,0])

dtr2_0 = np.array([-v0,0,0])

dtr3_0 = np.array([-v0,0,0])


init = np.array([0,1+R0,0,-np.cos(pi/6),-np.sin(pi/6)+R0,0,np.cos(pi/6),-np.sin(pi/6)+R0,0,
                 -v0,0,0,-v0,0,0,-v0,0,0])


def eq(arg,t):
    x1,y1,z1,x2,y2,z2,x3,y3,z3,dtx1,dty1,dtz1,dtx2,dty2,dtz2,dtx3,dty3,dtz3 = arg
    # las formas vectoriales del problema
    r1 = np.array([x1,y1,z1])
    r2 = np.array([x2,y2,z2])
    r3 = np.array([x3,y3,z3])
    dtr1 = np.array([dtx1,dty1,dtz1])
    dtr2 = np.array([dtx2,dty2,dtz2])
    dtr3 = np.array([dtx3,dty3,dtz3])
    # parte en x y en y de la ecuación:
    ddotx1 = q/m*(Etot(r1,r1,r2,r3)[0]+dtr1[1])
    ddotx2 = q/m*(Etot(r2,r1,r2,r3)[0]+dtr2[1])
    ddotx3 = q/m*(Etot(r3,r1,r2,r3)[0]+dtr3[1])
    ddoty1 = q/m*(Etot(r1,r1,r2,r3)[1]-dtr1[0])
    ddoty2 = q/m*(Etot(r2,r1,r2,r3)[1]-dtr2[0])
    ddoty3 = q/m*(Etot(r3,r1,r2,r3)[1]-dtr3[0])
    # parte en z de la ecuación:
    ddotz = 0
    # lo que retorna
    retval = [dtx1,dty1,dtz1,dtx2,dty2,dtz2,dtx3,dty3,dtz3,ddotx1,ddoty1,ddotz,ddotx2,ddoty2,ddotz,ddotx3,ddoty3,ddotz]
    return retval

sol = odeint(eq, init, t)

x1 = sol[:,0]
y1 = sol[:,1]
z1 = sol[:,2]
x2 = sol[:,3]
y2 = sol[:,4]
z2 = sol[:,5]
x3 = sol[:,6]
y3 = sol[:,7]
z3 = sol[:,8]

plt.title('Carga vs posición')
plt.plot(x1,y1,'crimson', label = 'Carga 1')
plt.plot(x2,y2,'darkviolet', label = 'Carga 2')
plt.plot(x3,y3,'springgreen', label = 'Carga 3')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.show()