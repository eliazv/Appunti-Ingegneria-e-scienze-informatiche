# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:13:56 2021

@author: Elia
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import sympy.utilities.lambdify as lambdify

x = sym.symbols('x')    

symf = x - (1/3)*sym.sqrt(30*x - 25) #funzione
symdf = sym.diff(symf, x, 1)    #derivata prima

f = lambdify(x, symf, np)   #valutare la funzione
df = lambdify(x, symdf, np)

#----------------------------PUNTO A-------------------------------------------
#si stabilisca quante radici reali ha f nell'intervallo [5/6, 25/6] e si giustifichi la risposta;

A, B = 5/6, 25/6
xx = np.linspace(A, B, 100)     #crea intervallo suddiviso in 100 parti



plt.title("f")
plt.plot(xx, f(xx), "-r")    #intervallo, funzione, colore
plt.plot(xx, xx*0, "-k")
plt.show()
#plt.plot(xx, df(xx), "-b")

#----------------------------PUNTO B-------------------------------------------
#si costruisca un metodo iterativo che, partendo da x(0) = 4, converga ad alpha (zero di f), quadraticamente;

symg = (1/3)*sym.sqrt(30*x - 25)
symdg = sym.diff(symf, x, 1)

g = lambdify(x, symg, np)
dg = lambdify(x, symdg, np)

plt.title("g")
plt.plot(xx, g(xx))
plt.plot(xx, xx)
plt.show()

plt.title("derivata di g")
plt.plot(xx, dg(xx), "-r")
plt.plot([A, B], [1, 1], "-k")
plt.plot([A, B], [-1, -1], "-k")
plt.show()

#iterazioneAPuntoFisso (in ZeridiFunzione)
def metodoIterativo(g, x0, tol, itmax):
    xk = []
    xk.append(x0)
    x1 = g(x0)
    xk.append(x1)
    it = 1
    d = x1 - x0
    
    while it < itmax and abs(d) > tol*abs(x1):
        x0 = x1
        x1 = g(x1)
        d = x1 - x0
        xk.append(x1)
        it = it+1
        
    if it == itmax:
        print("numero massimo di iterazioni raggiunto")
        
    return np.asarray(xk), it

xk, it = metodoIterativo(g, 4, 1.e-3, 100)      #perche questa tolleranza?
plt.plot(xk)
print(it)
print(xk[-1])
plt.show()
        
        
#----------------------------PUNTO C-------------------------------------------
     #si verifichi numericamente l'ordine di convergenza del metodo implementato al punto b);   

#stimaOrdine in zeridifunzione
def stimaConvergenza(xk, it):
    
    p = []
    for i in range(it-3):
        num = np.log(xk[i+2] - xk[i+3])/np.log(xk[i+1]-xk[i+2])
        den = np.log(xk[i+1] - xk[i+2])/np.log(xk[i]-xk[i+1])
        p.append(num/den)
        
    return p[-1]
        
print("ordine di convergenza = ", stimaConvergenza(xk, it))
        

#----------------------------PUNTO D-------------------------------------------
    #si rappresenti in un grafico in scala semilogaritmica sulle y ecc...

plt.semilogy(abs(xk))
plt.show()

#----------------------------PUNTO E-------------------------------------------
    # b puo convergere ad quadraticamente anche alpha partendo dall'estremo sinistro dell'intervallo

plt.title("derivata di g")
plt.plot(xx, dg(xx), "-r")
plt.plot([A, B], [1, 1], "-k")
plt.plot([A, B], [-1, -1], "-k")
plt.plot(5/6, dg(5/6), "x")
plt.show()


xk, it = metodoIterativo(g, 5/6, 1.e-3, 100)
plt.plot(xk)
print(it)
print(xk[-1])
plt.show()


