# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:28:43 2021

@author: Nicolò
"""

import numpy as np

def TrapComp(f, a, b, n):
    h = (b-a)/n
    
    x = np.arange(a, b+h, h)
    y = f(x)
    
    I = (y[0] + 2*np.sum(y[1:n]) + y[n])*(h/2)
    return I


# Stima del numero N si sottointervalli per approssimare l'integrale della
# funzione integranda con precisione tol
def TrapToll(f, a, b, toll):
    nMax = 2048
    n = 1
    err = 1
    
    In = TrapComp(f, a, b, n)
    while n <= nMax and err > toll:
        n = n*2
        I2n = TrapComp(f, a, b, n)
        err = abs(I2n - In)/3
        In = I2n
        
    if n > nMax:
        return 0, 0, 0
    
    return In, n, 1


#formula di Simpson Composita : 
def SimpComp(f, a, b, n):
    h = (b-a)/(n*2)
    
    x = np.arange(a, b+h, h)
    y = f(x)
    
    I = (y[0] + 2*np.sum(y[2:n*2:2]) + 4*np.sum(y[1:n*2:2]) + y[n])*(h/3)
    return I

#formula di Simpson .. : ricerca automatica del numero di N
#di sottointervalli
def SimpToll(f, a, b, toll):
    nMax = 2048
    n = 1
    err = 1
    
    In = TrapComp(f, a, b, n)  #simpcomp i altri es
    while n <= nMax and err > toll:
        n = n*2
        I2n = SimpComp(f, a, b, n)
        err = abs(I2n - In)/15
        In = I2n
        
    if n > nMax:
        print('Raggiunto nmax di intervalli con simptoll')
        return 0, 0, 0  # oppure  N=0  IN=[]
    
    return In, n, 1












