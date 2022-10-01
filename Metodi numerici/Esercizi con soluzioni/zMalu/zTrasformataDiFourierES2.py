# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:07:10 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import math

n = 3
A = -2#-math.pi
B = 2#math.pi
step = (B-A)/(n+1)
xx = np.arange(A, B, step)

f = lambda x : np.sinh(x)

#mappo i punti nell'intervallo 0-2pi
l = 0
r = 2*math.pi
xm=(xx-A)*(r-l)/(B-A)+l
 
m = n // 2  #// restituisce l'intero inferiore della divisione
   
y = f(xx)
c = fft(y) #calcola la trasformata di Fourier
a = np.zeros((m+2,)) #array che conterrà la parte reale
b = np.zeros((m+2,)) #array che conterrà la parte immaginaria


a0 = c[0]/(n+1)
a[1:m+1]=2*c[1:m+1].real/(n+1) 
b[1:m+1]=-2*c[1:m+1].imag/(n+1)

if n%2 != 0:
    a[m+1]=c[m+1]/(n+1) 


pol = a0*np.ones((100,))
z = np.linspace(A,B,100)
zm = (z-A)*(r-l)/(B-A)+l

for i in range(1,m+2):
   pol = pol + a[i]*np.cos(i*zm) + b[i]*np.sin(i*zm) 

plt.plot(z,pol,'-r')
plt.plot(xx,y ,'x')
plt.plot(z ,f(z),'-b')
plt.show()
