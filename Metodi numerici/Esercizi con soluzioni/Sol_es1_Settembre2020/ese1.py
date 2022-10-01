# -*- coding: utf-8 -*-
"""
Ese1
"""

import numpy as np
import matplotlib.pyplot as plt
from funzioni_zeri import newton_m, stima_ordine
import sympy as sym
from sympy.utilities.lambdify import lambdify


x=sym.symbols('x')
fx= x-2*sym.sqrt(x-1)
dfx=sym.diff(fx,x,1)
print('Derivta prima di f -->', dfx)
#In x=2 si annula sia la funzione che la sua derivata prima,
#la funzione ha in x=2 uno xero con molteplicita=2 
f=lambdify(x,fx,np)
fp=lambdify(x,dfx,np)

x=np.linspace(1,3,100)
plt.plot(x,f(x))
plt.plot(x,[0]*100)
plt.show()
x0=3
m=2
tolx=1e-12
tolf=1e-12
nmax=100

#Utilizzo il metodo di Newton Modificato con m=2
x1,it,xk= newton_m(f,fp,x0,m,tolx,tolf,nmax)
print('Zero ',x1,' individuato in ', it,' iterazioni')
#Verifico l'ordine di convergenza
ordine=stima_ordine(xk,it)
print('Ordine di convergenza ',ordine)
plt.semilogy(range(it),np.abs(xk))
plt.show()


#Il metodo non converge se scelgo come iterato iniziale x0=1,
#perchè la derivata prima in 1 divergem va a -infinito