# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:34:05 2021

@author: damia
"""

import numpy as np
import matplotlib.pyplot as plt
from  funzioni_Interpolazione_Polinomiale  import InterpL, plagr
from Funzioni_Integrazione import simptoll



f = lambda x: x-np.sqrt(x-1)

#----PUNTO A : Scrivere il proprio codice Matlab per determinare il polinomio p(x) di grado 3, in
#   forma di Newton, che interpola la funzione f(x) su nodi equispaziati.

#La funzione fpol è la funzione che valuta il polinomio interpolatore
# in un numpy array val

def fpol(val):
    pol=InterpL(x,y,val)    
    return pol 

#Estremi di integrazione

a=1
b=3
n=3

#Costruzione del polinomio di interpolazione di Lagrange di grado n=3
x=np.linspace(a,b,n+1)
y=f(x)
#Costruzione del numpy array z in cui valutare il polinomio interpolatore di Lagrange
z=np.linspace(a,b,100)
pol=InterpL(x,y,z)



#----PUNTO B : Disegnare in una stessa figura i punti di interpolazione, il grafico di f e del polinomio
#   di interpolazione p ottenuto al punto a).

#Grafico del polinomio interpolatore di Lagrange nei punti dell'array z
plt.plot(z,f(z),z,pol,x,y,'o')
plt.legend(['Funzione da interpolare','Polinomio interpolatore', 'Nodi di interpolazione'])
plt.show()



#----PUNTO C : Scrivere il proprio codice Matlab per calcolare con la formula di Simpson composita
#su N sottointervalli equispaziati, i valori approssimati ~I1 e ~I2 degli integrali

def SimpComp(fname,a,b,n):
    h=(b-a)/(2*n)
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[2:2*n:2])+4*np.sum(f[1:2*n:2])+f[2*n])*h/3
    return I        

def simptoll(fun,a,b,tol):
    Nmax=4096
    err=1
    N=1;
    IN=SimpComp(fun,a,b,N);
    while N<=Nmax and err>tol :
        N=2*N
        I2N=SimpComp(fun,a,b,N)
        err=abs(IN-I2N)/15
        IN=I2N
    if N>Nmax:
        print('Raggiunto nmax di intervalli con simptoll')
        N=0
        IN=[]
    return IN,N


#----PUNTO D : Si stimi il numero N di sottointervalli equispaziati che servono per approssimare con
#la formula di Simpson composita i due integrali (il cui valore esatto è rispettivamente
#I1 = 2:114381916835873 e I2 = 2:168048769926493) nel rispetto della tolleranza
#10^-5. Quanto vale N nei due casi? Quanto valgono |~I1 - I1| e |~I2 - I2|? Motivare i
#risultati ottenuti.


#Stima del numero N si sottointervalli per approssimare l'integrale della
# funzione integranda con precisione tol
tol=1e-5
I1t,N1=simptoll(f,a,b,tol)

#Stima del numero N si sottointervalli per approssimare l'integrale del
# polinomio interpolatore di grado 3 con precisione tol
I2t,N2=simptoll(fpol,a,b,tol)


#I1 ed I2 sono i valori esatti dei due integrali 
I1 = 2.114381916835873
I2 = 2.168048769926493

err1=abs(I1t-I1)
err2=abs(I2t-I2)

print('Errore integrale funzione f(x)', err1,' Numero di suddivisioni ', N1)
print('Errore integrale del polinomio interpolatore', err2, 'Numero di suddivisioni ',N2)

'''
Il numero di suddivisioni per il calcolo dell'integrale del polinomio interpolatore di grado
3 è uguale a 2 e l'errore commesso è dell'ordine di 1e-14, perchè l'errore
della formula di integrazione di Simpson dipende dalla derivata quarta della funzione integranda,
e poichè nel calcolo del secondo integrale, la funzione integranda è un polinomio di grado 3 che ha derivata
quarta nulla, non è necessario suddividere ancora l'intervallo di integrazione per ottenere
l'approssimazione dell'integrale con la precisione richiesta.
'''