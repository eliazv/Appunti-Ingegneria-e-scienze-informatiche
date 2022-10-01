# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:38:13 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt

# Restituisce i coefficienti del k-esimo pol di Lagrange associato ai punti del vettore xnodi
def PLagr(xnodi, k):

    xzeri=np.zeros_like(xnodi) #aggiunta
    n=xnodi.size  #aggiunta 

    if k==0:
       xzeri=xnodi[1:n]
    else:
       xzeri=np.append(xnodi[0:k],xnodi[k+1:n])
    
    num=np.poly(xzeri) #trova i coefficienti di un polinomio avente quella determinata sequenza di zeri
    den=np.polyval(num,xnodi[k]) #valuta il polinomio nello specifico valore xnodi[k]
    
    return num/den


 """"
        %funzione che determina in un insieme di punti il valore del polinomio
        %interpolante ottenuto dalla formula di Lagrange.
        % DATI INPUT
        %  xnodi  vettore con i nodi dell'interpolazione
        %  ynodi  vettore con i valori dei nodi 
        %  xx vettore con i punti in cui si vuole calcolare il polinomio
        % DATI OUTPUT
        %  y vettore contenente i valori assunti dal polinomio interpolante
        %
 """
def InterpL(xnodi, ynodi, xx):
    
     r=xnodi.size
     c=xx.size
     L=np.zeros((r,c))
     #calcolo tanti polinomi di lagrange quanti sono i nodi dell'interpolazione
     for k in range(r):
        p=PLagr(xnodi,k)
        L[k]=np.polyval(p,xx) #valuto il polinomio di lagrange di grado k nei valori xx
    
     return np.dot(ynodi, L)
 
    
f = lambda x : np.cos(np.pi * x) + np.sin(np.pi * x)
xx = np.linspace(0, 2, 100)
nodi = np.array([0.25, 0.75, 1, 1.5, 1.75])
plag = InterpL(nodi, f(nodi), xx)

plt.plot(xx, f(xx), "-r")
plt.plot(nodi, f(nodi), "x")
plt.plot(xx, plag, "-b")
plt.show()