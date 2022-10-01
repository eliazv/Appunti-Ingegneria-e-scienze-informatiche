# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:26:28 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt


def TrapComp(f, a, b, n):
    h = (b-a)/n
    xx = np.arange(a, b+h, h)
    fxx = f(xx)
    I = (fxx[0] + 2*np.sum(fxx[1:n]) + fxx[n]) * (h/2)
    return I

def TrapToll(f, a, b, toll):
    nMax = 2048
    n = 1
    err = 1
    
    In = TrapComp(f, a, b, n)
    
    while n <= nMax and err > toll:
        n = 2*n
        In2 = TrapComp(f, a, b, n)
        err = abs(In - In2)/3
        In = In2
        
    if n > nMax:
        return 0, 0, 0
        
    return In, n, 1

#-----------------------------PUNTO A------------------------------------------

a = 0
b = 1
tol = 1.e-6
Ia = np.zeros(30)
for n in range(0, 30):
    f = lambda x : (x**n)/(x+10)
    xx = np.linspace(a, b, 100)
    
    IN, N, flag = TrapToll(f, a, b, tol)
    Ia[n] = IN
    if flag == 1:
        print("n = ", str(n), "IN = ", str(IN), "N = ", str(N))
    else:
        print("n = ", str(n), " -> errore")

plt.plot(Ia)
plt.show()

#-----------------------------PUNTO B------------------------------------------

a = 0
b = 1
tol = 1.e-6
    
y = np.zeros(30)
y[0] = (np.log(11)-np.log(10))
for n in range(1, 30):
    y[n] = 1/n - 10*y[n-1]

err = abs(Ia - y)/abs(Ia)
plt.semilogy(err, "-b")

#-----------------------------PUNTO C------------------------------------------

a = 0
b = 1
tol = 1.e-6
    
z = np.zeros(30)
z[29] = 0
for n in range(29,0,-1):
    z[n-1]=1/10*(1/n-z[n])


err = abs(Ia - z)/abs(Ia)
plt.semilogy(err, "-r")
plt.show()













    