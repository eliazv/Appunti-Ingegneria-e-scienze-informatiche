# -*- coding: utf-8 -*-
"""
Created on Mon May 17 05:51:56 2021

@author: damia
"""
import numpy as np

def TrapComp(fname,a,b,n):
    h=(b-a)/n
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[1:n])+f[n])*h/2
    return I

    
def SimpComp(fname,a,b,n):
    h=(b-a)/(2*n)
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[2:2*n:2])+4*np.sum(f[1:2*n:2])+f[2*n])*h/3
    return I


def traptoll(fun,a,b,tol):

    Nmax=2048
    err=1
    
    N=1;
    IN=TrapComp(fun,a,b,N);
    
    while N<=Nmax and err>tol :
        N=2*N
        I2N=TrapComp(fun,a,b,N)
        err=abs(IN-I2N)/3
        IN=I2N
 
    
    if N>Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        N=0
        IN=[]
 
    return IN,N


def simptoll(fun,a,b,tol):

    Nmax=2048
    err=1
    
    N=1;
    IN=SimpComp(fun,a,b,N);
    
    while N<=Nmax and err>tol :
        N=2*N
        I2N=SimpComp(fun,a,b,N)
        err=abs(IN-I2N)/15
        IN=I2N
 
    
    if N>Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        N=0
        IN=[]
 
    return IN,N
