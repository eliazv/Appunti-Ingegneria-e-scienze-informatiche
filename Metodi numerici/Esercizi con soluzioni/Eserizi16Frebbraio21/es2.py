# -*- coding: utf-8 -*-
"""
ese2
"""


import numpy as np
import math
from funzioni_Interpolazione_Polinomiale import InterpL
import matplotlib.pyplot as plt
#nodi del problema di interpolazione 

#PUNTO A : Implementare la function InterpN.m che, presi in input i vettori contenenti le ascisse e le ordinate dei
#punti di interpolazione, calcoli il vettore dei coefficienti del polinomio di interpolazione espresso nella
#forma di Newton.
def InterpL(xnodi, ynodi, xx):
     r=xnodi.size
     c=xx.size
     L=np.zeros((r,c))
     for k in range(r):
        p=PLagr(xnodi,k)
        L[k]=np.polyval(p,xx) 
     return np.dot(ynodi, L)

#PUNTO B: hornerN.m non l'abbiamo fatto (?)


#PUNTO C : facendo uso delle functions implementate precedentemente, si determini il polinomio p che interpola
#f sui nodi 1.0,1.5,1.75
f= lambda x: np.cos(math.pi*x)+np.sin(math.pi*x)
x=np.array([1.0,1.5,1.75])
y=f(x)
# punti di valutazione per l'interpolante
xx=np.linspace(0.0,2.0,100)
pol=InterpL(x,y,xx)


#PUNTO D : si rappresenti in uno stesso graco la funzione f, il polinomio p e i punti di interpolazione assegnati;
plt.plot(xx,pol,'r-',xx,f(xx),'b--',x,y,'go')
plt.legend(['interpolante di Lagrange','Funzione da interpolare', 'nodi di interpolazione'])
plt.show()


#PUNTO E : si calcoli il valore assunto dalla funzione resto r(x) := |f(x) - p(x)| nel punto x* = 0:75;
polxs=InterpL(x,y,np.array([0.75]))
 
err_xs= np.abs(polxs-f(0.75))
print("Funzione resto nel nodo 0.75 uguale a ",err_xs)

#Poichè il resto nel punto x=0.75 è dell'ordine della precisione di macchina,
# si può concludere che il polinomio interpola anche il punto 0.75, per cui
# se si considera il polinomio che interpola i nodi

#PUNTO F : si stabilisca qual'e il polinomio interpolatore per f passante per i nodi x*, x0, x1 e x2.
#Verifica
x=np.array([0.75, 1.0,1.5,1.75])
y=f(x)
# punti di valutazione per l'interpolante
xx=np.linspace(0.0,2.0,100)
pol=InterpL(x,y,xx)
plt.plot(xx,pol,'r-',xx,f(xx),'b--',x,y,'go')
plt.legend(['interpolante di Lagrange con un nodo in più','Funzione da interpolare','nodi di interpolazione'])
 