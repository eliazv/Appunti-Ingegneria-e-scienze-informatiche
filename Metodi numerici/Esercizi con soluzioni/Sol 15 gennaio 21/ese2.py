# -*- coding: utf-8 -*-
"""
Esercizio 2 del 15 Gennaio
"""


import numpy as np
from funzioni_Sistemi_lineari import Lsolve, Usolve, LUsolve, LU_nopivot
from scipy.linalg import pascal


#PUNTO A : Scrivere la function LUnopivot.m che, presa in input una matrice A, restituisce in output le matrici
#   L e U associate al metodo di eliminazione gaussiana senza pivoting.

def LU_nopivot(A):
    m,n=A.shape   
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag
  
    P=np.eye(n);
    U=A.copy();

    for k in range(n-1):
 
          if U[k,k]==0:
            print('elemento diagonale nullo')
            L,U,P,flag=[],[],[],1 
            return P,L,U,flag

          U[k+1:n,k]=U[k+1:n,k]/U[k,k]                                   # Memorizza i moltiplicatori	  
          U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n])  # Eliminazione gaussiana sulla matrice
     
    L=np.tril(U,-1)+np.eye(n)  # Estrae i moltiplicatori 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,flag



#PUNTO B : Scrivere la function che implementa il metodo delle sostituzioni all'indietro per risolvere un sistema
#   lineare con matrice dei coecienti triangolare superiore.

def Lsolve(L,b):
    m,n=L.shape
    flag=0
    if n != m:
        print('errore: matrice non quadrata')
        flag=1
        x=[]
        return x, flag
    
     # Test singolarita'
    if np.all(np.diag(L)) != True:
         print('el. diag. nullo - matrice triangolare inferiore')
         x=[]
         flag=1
         return x, flag
    # Preallocazione vettore soluzione
    x=np.zeros((n,1))
    
    for i in range(n):
         s=np.dot(L[i,:i],x[:i]) #scalare=vettore riga * vettore colonna
         x[i]=(b[i]-s)/L[i,i]
      
    return x,flag



#PUNTO C : Scrivere la function che implementa il metodo delle sostituzioni in avanti per risolvere un sistema
#   lineare con matrice dei coecienti triangolare inferiore.

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



#PUNTO D
#Scrivere lo script Matlab es2.m in cui si sfruttano la fattorizzazione LU di A e le function implementate
#in b) e c) per calcolare le soluzioni dei sistemi lineari ATx=b  e  A2x=c  con A=pascal(n)  b=AT*ones(n,1)  c=A2*ones(n,1)


def  LULUsolve(L,U,c):
    #Soluzione del sistema lineare A**2 x= c che equivale a L U L U x =c
    y3,flag=Lsolve(L,c)
    y2,flag=Usolve(U,y3)
    y1,flag=Lsolve(L,y2)
    x,flag=Usolve(U,y1)
    return x


for n in range(5,11):
    
    #MAtrice di Pascal di ordine n, definita mediante la funzione pascal nel modulo scipy.linalg
    A=pascal(n)
    #Costruzione del termine noto del primo sistema lineare
    b=np.dot(A.T,np.ones((n,1)))
    #Costruzione del termine noto del secondo sistema lineare
    c=np.dot(np.dot(A,A),np.ones((n,1)))
    #Fattorizzazione senza strategia del pivoting della matrice A
    P,L,U,flag=LU_nopivot(A)
    #Soluzione del sistema A.T x =b, (che equivake a U.T L.T x=b )
    x1,flag=LUsolve(U.T,L.T,P,b)
    print('Soluzione sistema 1 \n ',x1)
    #Soluzione del sistema A**2 x=c, (che equivake a L U L U x= c)
    x2=LULUsolve(L,U,c)
    print('Soluzione sistema 2 \n', x2)
    


 #PUNTO E   
'''   
Conviene utilizzare la strategia proposta per la soluzione del sistema 2, perchè se la matrice A
è mal condizionata, il sistema lineare con matrice A**2 ha un indice di condizionamento dell'ordine del suo
quadrato, quindi conviene risolvere i 4 sistemi lineari con matrici triangolari che hanno indice di
condizionamento sicuramente minore di A**2
'''