# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:05:46 2021

@author: Nicolò
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fft  import fft, ifft
from scipy.fftpack import fftshift, ifftshift

A, B = 0, 2
l, r = 0, 2*math.pi
n = 200
step = (B-A)/(n+1)

f = lambda x : np.sin(2*np.pi*5*x) + np.sin(2*np.pi*10*x)
noise = lambda x : np.sin(2*np.pi*30*x)

#-----------------------------SEGNALE RUMOROSO---------------------------------
plt.title("Segnale rumoroso")
x = np.linspace(A, B, n)
y = noise(x) + f(x)

plt.plot(x, y, "-r")
plt.show()

c = fftshift(fft(y))


#------------------------SPETTRO SEGNALE RUMOROSO------------------------------
plt.title("Spettro segnale rumoroso")

freq=np.arange(-50,50,0.5)
plt.plot(freq, abs(c))
plt.show()

#------------------------SPETTRO SEGNALE FILTRATO------------------------------
plt.title("Spettro segnale filtrato")

for i in range(len(freq)):
    if abs(freq[i]) > 10:
        c[i] = 0
        
freq=np.arange(-50,50,0.5)
plt.plot(freq, abs(c))
plt.show()

#-----------------------RICOSTRUZIONE SEGNALE FILTRATO-------------------------

yricostruita = ifft(ifftshift(c))

x = np.linspace(A, B, n)
plt.plot(x, f(x), "-b")
plt.plot(x, yricostruita, "-r")
plt.show()