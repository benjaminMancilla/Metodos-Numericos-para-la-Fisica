# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:48:51 2022

@author: benja
"""

import numpy as np
import T2P2 as t2

def FthetaFuera(theta):
    return 1j*((np.e**(np.e**(2j*theta)+1j*theta))/(np.e**(1j*theta)-2))

def FthetaDentro(theta):
    return 1j*(np.e**((np.e**(2j*theta))+(4*np.e**(1j*theta))+4))

def prueba():
    return np.e**(4)*2*np.pi*1j
n=100000*40
I1 = t2.Simpson(0, 2*np.pi, n, FthetaFuera)
I2 = t2.Simpson(0, 2*np.pi, n, FthetaDentro)

print(str(I1) + " es el valor que entrega fuera del circulo." )
print(str(I2) + " es el valor que entrega dentro del circulo.")



