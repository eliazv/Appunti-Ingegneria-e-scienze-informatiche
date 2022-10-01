# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:20:14 2021

@author: Nicolò
"""

import numpy as np

def L_solve(L,b):
    m,n=L.shape
    #<controllo se m è diverso da n. se si esco con flag di errore>
    #<controllo se c'è un elemento diagonale nullo. se c'è esco dando errore>
    if np.all(np.diag(L)) != True:
         return [], 1
     
    x=np.zeros((n,1))#prealloco il vettore soluzione
    
    #ciclo su tutte le righe della matrice
    for i in range(n):
         somm=np.dot(L[i,:i],x[:i]) #scalare=vettore riga * vettore colonna
         x[i]=(b[i]-somm)/L[i,i]
      
    return x,0

def U_solve(U,b):
    m,n=U.shape
    #<controllo se m è diverso da n. se si esco con flag di errore>
    #<controllo se c'è un elemento diagonale nullo. se c'è esco dando errore>
    if np.all(np.diag(U)) != True:
         return [], 1
     
    x=np.zeros(n)#prealloco il vettore soluzione
    
    #ciclo su tutte le righe della matrice (partendo dall'ultima e arrivando alla prima)
    for i in range(n-1,-1,-1):
         somm=np.dot(U[i,i+1:],x[i+1:]) #scalare=vettore riga * vettore colonna
         x[i]=(b[i]-somm)/U[i,i]
      
    return x,0

def swapRows(A,k,p):
    A[[k,p]] = A[[p,k]]

#in esercizio
def swapRows2(A,k,p):
    A[[k,p],:] = A[[p,k],:]
    

"""
    % Fattorizzazione PA=LU con pivot 
    In output:
    L matrice triangolare inferiore
    U matrice triangolare superiore
    P matrice di permutazione
    tali che  PA=LU
    """
def LU_nopivot(A):
    m,n=A.shape
    #<controllo se m è diverso da n. se si esco con flag di errore>
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag

    P=np.eye(n); #senza pivoting P è semplicemente l'identità
    U=A.copy(); #U inizialmente è la copia di A
    
    for k in range(n-1): #ciclo su tutte le colonne di U tranne l'ultima
        #<controllo se il pivot (U[k,k]) è zero. se è zero esco con flag di errore
        #eliminazione gaussiana
        U[k+1:n,k]=U[k+1:n,k]/U[k,k]  #Memorizza i moltiplicatori
        U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n])  #Eliminazione gaussiana sulla matrice
    
    #N.B. il -1 nel tril. la diagonale in L è SEMPRE di soli uno
    L=np.tril(U,-1)+np.eye(n) #L è la matrice triangolare inferiore. 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,0

def LU_pivot(A):
    m,n=A.shape
    #<controllo se m è diverso da n. se si esco con flag di errore>
    P=np.eye(n); #usando il pivoting P potrebbe cambiare
    U=A.copy(); #U inizialmente è la copia di A
    
    for k in range(n-1): #ciclo su tutte le colonne di U tranne l'ultima
    
        #fissata la colonna k cerco l'indice con elemento in valore assoluto maggiore dalla diagonale in giù
        #(unica differenza tra con e senza pivoting)
        p = np.argmax(abs(U[k:n,k])) + k
        if p != k: #se l'elemento trovato non è il pivot lo scambio
            swapRows(P,k,p)
            swapRows(U,k,p)
        #eliminazione gaussiana
        U[k+1:n,k]=U[k+1:n,k]/U[k,k]  #Memorizza i moltiplicatori
        U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n])  #Eliminazione gaussiana sulla matrice
        
    #N.B. il -1 nel tril. la diagonale in L è SEMPRE di soli uno
    L=np.tril(U,-1)+np.eye(n) #L è la matrice triangolare inferiore. 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,0

def LU_solve(L, U, P, b):
    Pb = np.dot(P, b) #moltiplicando b per P ne scambio le righe
    y, flag = L_solve(L, b) #risolvo Ly = Pb trovando y, ovvero Ux
    #<controllo il flag, se non va bene esco restituendo errore>
    x, flag = U_solve(U, y) #risolvo Ux = y trovando x
    return x

