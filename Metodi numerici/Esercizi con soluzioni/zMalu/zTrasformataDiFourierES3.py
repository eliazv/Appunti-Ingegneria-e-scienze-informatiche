# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 15:07:57 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.fft import fft

A, B = 0, 1
l, r = 0, 2*math.pi
n = 9
step = (B-A)/(n+1)

x = np.arange(0, 1, 0.1)
y = np.array([3.7, 13.5, 5, 4.6, 4.1, 4.5, 4, 3.8, 3.7, 3.7])


m = n//2

a = np.zeros((m+2, ))
b = np.zeros((m+2, ))
c = fft(y)

a0 = c[0]/(n+1)

a[1:m+1] = 2*c[1:m+1].real/(n+1)
b[1:m+1] = -2*c[1:m+1].imag/(n+1) 

if n%2 != 0:
    a[m+1] = c[m+1]/(n+1)
    
pol = a0 * np.ones((100, ))
z = np.linspace(A, B, 100)
zm = ((z-A)*(r-l)/(B-A) + l)

for i in range(1, m+2):
    pol = pol + a[i]*np.cos(i*zm) + b[i]*np.sin(i*zm)
    
    plt.plot(z, pol, "-r")
    plt.plot(x, y, "x")
    plt.show()








