# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:34:05 2021

@author: damia
"""

import numpy as np
import matplotlib.pyplot as plt
from Funzioni_Integrazione import traptoll


#----PUNTO A : si approssima In, n = 1; : : : ; 30 utilizzando la formula dei trapezi composita su N sottointervalli
#equispaziati, determinando automaticamente il valore di N affinchè il resto della formula di quadratura composita sia minore di tol = 1.e-6

#Estremi di integrazione
a=0
b=1
I=[]
#Stima del numero N si sottointervalli per approssimare l'integrale della
#funzione integranda con precisione tol
for n in range(1,31):
    f= lambda x: x**n/(x+10)
    tol=1e-6
    I1t,N1=traptoll(f,a,b,tol)
    I.append(I1t)


plt.plot(I,'r-o')
plt.show()

#----PUNTO B : si approssima In, n = 1; : : : ; 30 con il valore yn, n = 1; : : : ; 30 ottenuto dall'algoritmo ricorsivo   y1 = log(11)-log(10)   yn+1 = 1/n - 10yn;   n = 1;...; 29
nval=30
y=np.zeros((n,),dtype=float)
y[0]=np.log(11)-np.log(10)
for n in range(1,nval):
    y[n]=1/n-10*y[n-1]
    
    
err_rel_y=np.abs(y-I)/np.abs(I)
 

#----PUNTO C : si approssima In, n = 1; : : : ; 30 con il valore zn, n = 1; : : : ; 30 ottenuto dall'algoritmo ricorsivo   z31 = 0   zn=1/10(1/n - zn+1)  n=30,...,1
z=np.zeros((nval+1,),dtype=float)
z[nval]=0.0
for n in range(nval,0,-1):
    z[n-1]=1/10*(1/n-z[n])


#----PUNTO D :   si rappresenti in un grafico in scala semilogaritmica sulle y (comando semilogy)
#- l'andamento dell'errore relativo tra yn e In,
#- l'andamento dell'errore relativo tra zn e In,
#al variare di n = 1; : : : ; 30, assumendo come valore esatto per In quello calcolato al punto a);
err_rel_z=np.abs(z[0:nval]-I)/np.abs(I)
plt.semilogy(np.arange(nval),err_rel_y,'g-.',np.arange(nval),err_rel_z,'b--')
plt.legend(['Errore relativo algoritmo b ', 'Errore relativo algoritmo c'])


#----PUNTO E : osservando il grafico ottenuto in d), si stabilisca quale tra gli algoritmi in b) e c) risulta essere piu stabile.
#L'algoritmo piu' stabile e' l'algoritmo c)