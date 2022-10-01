# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:23:27 2021

@author: damia
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as spl


#----------------------------PUNTO A-------------------------------------------
#Scrivere la function Matlab Usolve.m che implementa il metodo delle sostituzioni all'indietro per risolvere un sistema lineare con matrice dei coecienti triangolare superiore.
def Usolve(U,b):
    m,n=U.shape
    flag=0;
    if n != m:
        print('errore: matrice non quadrata')
        flag=1
        x=[]
        return x, flag
    
     # Test singolarita'
    if np.all(np.diag(U)) != True:
         print('el. diag. nullo - matrice triangolare superiore')
         x=[]
         flag=1
         return x, flag
    # Preallocazione vettore soluzione
    x=np.zeros((n,1))
    
    for i in range(n-1,-1,-1):
         s=np.dot(U[i,i+1:n],x[i+1:n]) #scalare=vettore riga * vettore colonna
         x[i]=(b[i]-s)/U[i,i]
      
     
    return x,flag

#----------------------------PUNTO B-------------------------------------------
"""     
Scrivere la function Matlab metodoQR.m che, presi in input due vettori contenenti rispettivamente le
ascisse e le ordinate dei punti da approssimare ai minimi quadrati, determini i coefficienti del poli-
nomio di approssimazione di grado n risolvendo un opportuno sistema lineare tramite chiamata della
function Usolve.
"""
def metodoQR(x,y,n):
    H=np.vander(x,n+1)
    Q,R=spl.qr(H)
    y1=np.dot(Q.T,y)
    a,flag=Usolve(R[0:n+1,:],y1[0:n+1])
    return  a

#----------------------------PUNTO C-------------------------------------------
""" 
Si utilizzi la function Matlab metodoQR per determinare i polinomi di approssimazione ai minimi qua-
drati di grado 1, 2 e 3 dei dati assegnati in tabella, e si rappresentino in uno stesso graFIco i dati
(xi; yi), i = 1;...; 12 e i tre polinomi determinati.
"""
#Script

m=12

x=np.linspace(1900,2010,12) #1900, 1910, 1920, ... , 2010.
y=np.array([76.0,92.0,106.0,123.0,132.0,151.0,179.0,203.0,226.0,249.0,281.0,305.0])


xmin=np.min(x)
xmax=np.max(x)
xval=np.linspace(xmin,xmax,100)



for n in range(1,4):
    a=metodoQR(x,y,n)
    residuo=np.linalg.norm(y-np.polyval(a,x))**2
    print("Norma del residuo al quadrato",residuo)
    p=np.polyval(a,xval)
    plt.plot(xval,p)
    

plt.legend(['n=1','n=2','n=3'])
 
plt.plot(x,y,'o')

#----------------------------PUNTO D-------------------------------------------
#Quale tra le tre approssimazioni ottenute al punto precedente risulta migliore? Confrontare gli errori
#dove f1, f2 e f3 denotano i polinomi di approssimazione di grado 1, 2 e 3 determinati al punto c).