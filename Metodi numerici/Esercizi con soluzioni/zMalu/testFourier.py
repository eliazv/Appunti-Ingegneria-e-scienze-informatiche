# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:24:04 2021

@author: Nicolò
"""

from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt
import math

A = -3
B = 3


n=int(input("n = "))
step = (B-A)/(n+1)
xx = np.arange(A, B, step)
y = []

i = 0
for xi in xx:
    if xi <= -1 or xi > 1:    
        y.append(1)
    else:
        y.append(0)
    i = i+1
    
m = n//2
l, r = 0, 2*math.pi
c = fft(y)
a = np.zeros((m+2, ))
b = np.zeros((m+2, ))

a0 = c[0]/(n+1)
a[1:m+1] = 2*c[1:m+1].real/(n+1)
b[1:m+1] = -2*c[1:m+1].imag/(n+1)

if n%2 != 0:
    a[m+1] = c[m+1]/(n+1)
    
pol = a0*np.ones((100, ))
z = np.linspace(A, B, 100)
zm = (z-A)*(r-l)/(B-A)+l

for i in range(1, m+2):
    pol = pol + a[i]*np.cos(i*zm) + b[i]*np.sin(i*zm)
    
    title = "n = " + str(n)
    plt.title(title)
    plt.plot(z, pol, "-r")
    plt.plot(xx, y, 'x')
    plt.show()
    

    