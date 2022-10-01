# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 09:36:21 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym
import ZeriDiFunzione as zeri
import sympy.utilities.lambdify as lambdify

a = 1
b = 2
tol = 1.E-10
xx = np.linspace(a, b, 100)
x = sym.symbols('x')

simbF = 0.5 * sym.sqrt(10 - x**3) - 1
f = lambdify(x, simbF, np)
df = lambdify(x, sym.diff(simbF, x), np)

plt.plot(xx, f(xx), xx, xx*0)
plt.show()

plt.plot(xx, df(xx), "r")
plt.plot([a, b], [1, 1])
plt.plot([a, b], [-1, -1])
plt.show()

#---------------------BISEZIONE------------------------------------------------

x, it, flag = zeri.bisezione(f,a,b,tol)
if flag == 0:
    print("it = ", str(it), "; x = ", x[-1])
else:
    print("errore")

#--------------------REGULA FALSI----------------------------------------------

x, it, flag = zeri.regulaFalsi(f, a, b, tol, 30)
if flag == 0:
    print("it = ", str(it), "; x = ", x[-1])
else:
    print("errore")

#--------------------CORDE----------------------------------------------

x, it, flag = zeri.corde(f, df, 1.4, tol, tol, 30)
if flag == 0:
    print("it = ", str(it), "; x = ", x[-1])
else:
    print("errore")