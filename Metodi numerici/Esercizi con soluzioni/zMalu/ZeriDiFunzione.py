# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:13:03 2021

@author: Nicolò
"""

import numpy as np
import math

def concordi(x1, x2):
    return math.copysign(1, x1) == math.copysign(1, x2)

def bisezione(f,a,b,tol):
    
    eps=np.spacing(1)
    x = [] #sequenza delle x trovate 
    it = 0 #numero di iterazioni effettuate
    
    if concordi(f(a), f(b)):
        print("errore, estremi concordi")
        return [], 0, 1
    
    maxit=int(math.ceil(math.log((b-a)/tol)/math.log(2))) #massimo numero di iterazioni previste
    
    while it < maxit and abs(b-a)>=tol+eps*max(abs(a),abs(b)):
        it = it+1
        c = a + (b-a)/2
        x.append(c)
        
        if f(c) == 0:
            break
        if concordi(f(a), f(c)):
            a = c
        else:
            b = c
    return x, it, 0

def regulaFalsi(f, a, b, tol, itmax):
    eps=np.spacing(1)
    xk = [] #sequenza delle x trovate 
    it = 0 #numero di iterazioni effettuate
    x = a
    
    if concordi(f(a), f(b)):
        print("errore, estremi concordi")
        return [], 0, 1
    
    while it < itmax and abs(b-a) >= tol+eps*max(abs(a),abs(b)) and abs(f(x))>=tol:
        it = it+1
        x=a-f(a)*(b-a)/(f(b)-f(a)); #Calcola l'intersezione tra l'asse x e la retta che passa per gli estremi
        xk.append(x)
        if f(x) == 0:
            break
        if concordi(f(a), f(x)):
            a = x
        else:
            b = x
    
    return xk, it, 0


def corde(f, df, x0, tolx, tolf, itmax):
    x = [] #sequenza delle x trovate 
    it = 0 #numero di iterazioni effettuate
    m = df(x0) #calcolo il coeff.angolare
    
    d = f(x0)/m
    x1 = x0 - d # d è ciò che devo sottrarre da x0 per ottenere x1
    x.append(x1)
    it = it+1
    
    while it < itmax and abs(f(x1))>=tolf and abs(d)>=tolx*abs(x1):
        x0 = x1
        d = f(x0)/m
        x1 = x0 - d
        x.append(x1)
        it = it+1
        
    return x, it, 0


def secanti(f,x0,x1,tolx,tolf,itmax):
        xk=[] #sequenza delle x trovate
        d=f(x1)*(x1-x0)/(f(x1)-f(x0)) 
        x2=x1-d
        xk.append(x2)
        it=1
       
        while it<itmax and abs(f(x2))>=tolf and abs(d)>=tolx*abs(x2):
            x0=x1
            x1=x2 
            d=f(x1)*(x1-x0)/(f(x1)-f(x0))
            x2=x1-d
            xk.append(x2)
            it=it+1
        
        return xk,it
    
    
def newton(f,df,x0,tolx,tolf,itmax):
        xk=[]
        eps = np.spacing(1)
        
        if abs(df(x0))>eps:
            d=f(x0)/df(x0)
            x1=x0-d
            xk.append(x1) #Aggiunge x1 alla successione di elementi
            it=0
           
        else:
            print('Newton:  Derivata nulla in x0 - EXIT \n')
            return [],0,0
        
        it=1
        while it<itmax and abs(f(x1))>=tolf and  abs(d)>=tolx*abs(x1):
            x0=x1
            if abs(df(x0))>eps:
                d=f(x0)/df(x0)
                x1=x0-d
                xk.append(x1)
                it=it+1
            else:
                 print('Newton: Derivata nulla in x0 - EXIT \n')
                 return xk, it, 1           
        
        return xk, it, 0


def newtonModificato(f,df,x0, m, tolx,tolf,itmax):
        xk=[]
        eps = np.spacing(1)
        
        if abs(df(x0))>eps:
            d=f(x0)/df(x0)
            x1=x0-d*m
            xk.append(x1) #Aggiunge x1 alla successione di elementi
            it=0
           
        else:
            print('Newton:  Derivata nulla in x0 - EXIT \n')
            return [],0,0
        
        it=1
        while it<itmax and abs(f(x1))>=tolf and  abs(d)>=tolx*abs(x1):
            x0=x1
            if abs(df(x0))>eps:
                d=f(x0)/df(x0)
                x1=x0-d*m
                xk.append(x1)
                it=it+1
            else:
                 print('Newton: Derivata nulla in x0 - EXIT \n')
                 return xk, it, 1           
        
        return xk, it, 0



"""
inputs funzione di iterazione, approssimazione iniziale, tolleranza e numero massimo di iterazioni.
outputs la soluzione sol dell'equazione non lineare, il numero di iterazioni compiute iter e il vettore delle approssimazioni xk.
"""
def iterazioneAPuntoFisso(g,x0,tolx,itmax):
    xk=[]
    xk.append(x0)
    x1=g(x0) #La nuova x è la x0 calcolata nella funzione g(x)
    d=x1-x0
    xk.append(x1)
    it=1
    while it<itmax and  abs(d)>=tolx*abs(x1) :
        x0=x1
        x1=g(x0) #La nuova x è la x0 calcolata nella funzione g(x)
        d=x1-x0 #Differenza tra le due iterate per la CONDIZIONE di ARRESTO
        it=it+1 #Incremento l'iterata
        xk.append(x1)
    
    return x1, it,xk


"""
Per verificare numericamente l'ordine di convergenza (stimaConvergenza).
Ha bisogno di 3 valori per questo calcolo xk xk-1 e xk-2, in particolare degli ultimi 3 che sono stati iterati.
"""
def stimaOrdine(xk,it):
    p=[]

    #Fa un ciclo prendendo gli ultimi 3 valori della successione di iterati.
    for k in range(it-3): 
        num = np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))
        den = np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1]))
        p.append(num/den);
   
    ordine=p[-1]
    return ordine