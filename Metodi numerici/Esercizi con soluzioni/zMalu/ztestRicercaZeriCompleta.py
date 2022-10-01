# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:26:41 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import sympy as sym
import sympy.utilities.lambdify as lambdify
import math

def stimaOrdine(xk, it):
    p = []
    for i in range(it-3):
        num = np.log(abs(xk[i+2]-xk[i+3])/abs(xk[i+1]-xk[i+2]))
        den = np.log(abs(xk[i+1]-xk[i+2])/abs(xk[i]-xk[i+1]))
        p.append(num/den)
    return p[-1]

def concordi(a, b):
    if math.copysign(1, a) == math.copysign(1, b):
        return True
    return False

def bisezione(f, a, b, tolx):
    xk = []
    it = 1
    itmax = math.ceil(math.log((b-a)/tolx)/math.log(2))
    
    if concordi(f(a), f(b)):
        print("Errore, estremi concordi")
        return [], [], 1
    
    c = a + (b-a)/2
    xk.append(c)
    if concordi(f(a), f(c)):
        a = c
    else:
        b = c
    d = a - b
    
    while it < itmax and abs(d) > tolx*max(abs(a), abs(b)):
        c = a + (b-a)/2
        xk.append(c)
        if concordi(f(a), f(c)):
            a = c
        else:
            b = c
        
        d = a - b
        it = it+1
        
    if it == itmax:
        print("Errore, numero massimo di iterazioni raggiunto")
        return [], [], 1
    
    return xk, it, 0

def regulaFalsi(f, a, b, tolx, toly, itmax):
    it = 1
    
    if concordi(f(a), f(b)):
        print("Errore, estremi concordi")
        return [], [], 1
    
    d = b-a
    x = a
    
    while it < itmax and abs(d) > tolx*max(abs(a), abs(b)) and abs(f(x)) > toly:
        m = (f(b)-f(a))/(b-a)
        x = a - f(a)/m
        
        if concordi(f(a), f(x)):
            a = x
        else:
            b = x
            
        xk.append(x)
        d = b-a
        it = it+1

    if it == itmax:
       print("Errore, numero massimo di iterazioni raggiunto")
       return [], [], 1
    
    return xk, it, 0

def corde(f, df, x0, tolx, toly, itmax):
    it = 1
    xk = []
    m = df(x0)
    d = f(x0)/m
    x1 = x0 - d
    xk.append(x1)
    
    while it < itmax and abs(d) > tolx*abs(x1) and abs(f(x1)) > toly:
        d = f(x1)/m
        x1 = x1 - d
        xk.append(x1)
        it = it+1
        
    if it == itmax:
       print("Errore, numero massimo di iterazioni raggiunto")
       return [], [], 1
    
    return xk, it, 0

def secanti(f, x0, x1, tolx, toly, itmax):
    it = 1
    xk = []
    m = (f(x1)-f(x0))/(x1-x0)
    d = f(x1)/m
    x2 = x1 - d
    xk.append(x2)

    while it < itmax and abs(d) > tolx*abs(x2) and abs(f(x2)) > toly:
        x0 = x1
        x1 = x2
        m = (f(x1)-f(x0))/(x1-x0)
        d = f(x1)/m
        x2 = x1 - d
        xk.append(x2)
        it = it+1
    
    if it == itmax:
        print("Errore, numero massimo di iterazioni raggiunto")
        return [], [], 1
    
    return xk, it, 0

def newton(f, df, x0, tolx, toly, itmax):
    it = 1
    xk = []
    
    d = f(x0)/df(x0)
    x1 = x0 - d
    xk.append(x1)
    
    while it < itmax and abs(d) > tolx*abs(x1) and abs(f(x1)) > toly:
        x0 = x1
        d = f(x0)/df(x0)
        x1 = x0 - d
        xk.append(x1)
        it = it+1
        
    if it == itmax:
      print("Errore, numero massimo di iterazioni raggiunto")
      return [], [], 1
    
    return xk, it, 0  

def puntoFisso(g, x0, tol, itmax):
    it = 1
    xk = []
    
    xk.append(x0)
    x1 = g(x0)
    d = x1 - x0
    xk.append(x1)
    
    while it < itmax and abs(d) > tolx*abs(x1):
        x0 = x1
        x1 = g(x0)
        d = x1 - x0
        xk.append(x1)
        it = it+1
        
    if it == itmax:
      print("Errore, numero massimo di iterazioni raggiunto")
      return [], [], 1
    
    return xk, it, 0
        
#---------------------------------TEST-----------------------------------------

A = 0
B = 3
tolx = 1e-7
toly = 1e-7
itmax = 100

xx = np.linspace(A, B, 100)

x = sym.symbols('x')
symF = x**2 + sym.cos(x**3 - 2) - 3.5

f = lambdify(x, symF, np)
plt.plot(xx, f(xx))
plt.plot(xx, xx*0)
plt.show()

SymDf = sym.diff(symF, x, 1)
df = lambdify(x, SymDf, np)
plt.plot(xx, df(xx), "-r")
plt.plot([A, B], [1, 1], "-k")
plt.plot([A, B], [-1, -1], "-k")
plt.show()

#-----------------------------RISULTATO ESATTO---------------------------------

alfa= fsolve(f, 2)
print("risultato esatto: alfa = ", alfa)

#------------------------------BISEZIONE---------------------------------------

xk, it, flag = bisezione(f, A, B, tolx)
p = stimaOrdine(xk, it)
print("bisezione: a = ", xk[-1], "; iterazioni = ", it, "; ordine: p = ", p)

#----------------------------REGULA FALSI--------------------------------------

xk, it, flag = regulaFalsi(f, A, B, tolx, toly, itmax)
p = stimaOrdine(xk, it)
print("reg falsi: a = ", xk[-1], "; iterazioni = ", it, "; ordine: p = ", p)

#------------------------------CORDE-------------------------------------------

xk, it, flag = corde(f, df, 3, tolx, toly, itmax)
p = stimaOrdine(xk, it)
print("corde: a = ", xk[-1], "; iterazioni = ", it, "; ordine: p = ", p)

#-----------------------------SECANTI------------------------------------------

xk, it, flag = secanti(f, 2, 3, tolx, toly, itmax)
p = stimaOrdine(xk, it)
print("secanti: a = ", xk[-1], "; iterazioni = ", it, "; ordine: p = ", p)

#-----------------------------NEWTON-------------------------------------------

xk, it, flag = newton(f, df, 2.5, tolx, toly, itmax)
p = stimaOrdine(xk, it)
print("newton: a = ", xk[-1], "; iterazioni = ", it, "; ordine: p = ", p)

#--------------------------PUNTO FISSO-----------------------------------------

symG = sym.sqrt(-sym.cos(x**3-2) + 3.5)
symDg = sym.diff(symG, x, 1)

g = lambdify(x, symG, np)
dg = lambdify(x, symDg, np)

plt.plot(xx, g(xx), "-r")
plt.plot(xx, xx, "-k")
plt.show()

plt.plot(xx, dg(xx), "-r")
plt.plot([A, B], [1, 1], "-k")
plt.plot([A, B], [-1, -1], "-k")
plt.show()


xk, it, flag = puntoFisso(g, 1.8, tolx, itmax)
if flag == 0:
    p = stimaOrdine(xk, it)
    print("punto fisso: a = ", xk[-1], "; iterazioni = ", it, "; ordine: p = ", p)
























