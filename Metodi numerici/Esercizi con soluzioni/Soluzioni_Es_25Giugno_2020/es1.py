# -*- coding: utf-8 -*-
"""
Created on Sat May 22 11:34:05 2021

@author: damia
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as npl
from funzioni_Sistemi_lineari import LU_nopivot



A=np.array([ [10, -4, 4, 0], [-4, 10, 0, 2], [4, 0, 10, 2], [0, 2, 2, 0]],dtype=float)
B=np.array([[5, -2, 2, 0], [-2, 5, 0, 1], [2, 0, 5, 1], [0, 1, 1, 5]],dtype=float)   

#PUNTO B : Stabilire se le matrici A e B ammettono la fattorizzazione LU senza pivoting, motivandone la risposta.

#Le matrici A e B ammettono fattorizzazione LU senza pivoting parziale a perno massimo?
#Verifico le ipotesi del teorema che garantisce che una matrice A ammetta fattorizzazione LU di gauss
#No pivoting, cioè che i minori principali abbiano rango massimo ((determinante diverso da zero))


det_minoreA=[]
for i in range (0,4):
    det_minoreA.append(npl.det(A[:i+1,:i+1]))

if np.all(det_minoreA!=0):
    print("La matrice A ammette fattorizzazione LU no-pivoting")

det_minoreB=[]
for i in range (0,4):
    det_minoreB.append(npl.det(B[:i+1,:i+1]))
    
if np.all(det_minoreB!=0):
    print("La matrice B ammette fattorizzazione LU no-pivoting")


#PUNTO C : Scrivere una function Matlab che, presa in input una matrice M che ammette fattorizzazione LU senza
#   pivoting, calcoli e restituisca in output le matrici di tale fattorizzazione.
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


P,L,U,flag= LU_nopivot(A)




#PUNTO D : Scrivere uno script che sfrutti l'output dell'algoritmo di fattorizzazione LU senza pivoting per calcolare
#nella maniera piu efficiente possibile sia il determinante di M che il determinante di M^-1.
#Eseguire lo script scegliendo come matrice M le matrici per cui al punto b) si è mostrata l'esistenza
#della fattorizzazione LU senza pivoting.

'''
Il determinante della matrice è uguale al prodotto degli elementi diagonali della matrice U
'''

detA=np.prod(np.diag(U))
print("Determinante della matrice A ",detA)


'''
Il determinante dell'inversa di una matrice è uguale al reciproco del
determinante della matrice di partenza
'''

detinvA=1/detA
print("Determinante dell'inversa di A ",detinvA)

P,L,U,flag= LU_nopivot(B)
detB=np.prod(np.diag(U))
print("Determinante della matrice A ",detB)
detinvB=1/detB
print("Determinante dell'inversa di B ",detinvB)