#Ese1

import numpy as np
import numpy.linalg as npl
from funzioni_Sistemi_lineari import LU_nopivot, solve_nsis_f

#----PUNTO A : si costruisca la matrice A = I - B, si calcoli M = maxi;j=1;...;5 |ai;j| e si verifichi che M < 1/5 ;

B=np.array([[0.98, 0.02, 0, 0.04, 0],
    [0.08, 0.93, 0.08, -0.07, -0.03],
    [0.04, 0.01, 0.97, -0.07, -0.04],
    [0.02, -0.03, 0, 1.03, 0],
    [0.07, 0.04, 0, -0.08, 1.01]])

n=5

I=np.eye(n)

A=I-B

#Calcolo l'inversa di B con il metodo inv del modulo numpy.linalg
invB=npl.inv(B)

M=np.max(np.abs(A))

#---PUNTO B : essendo M < 1/5 condizione sufficiente per garantire che ... converga e abbia somma (I - A)^-1,
#   si calcoli un'approssimazione dell'inversa di B mediante l'espressione ...

#Se M<1/5 calcolo l'approssimazione dell'inversa di B
#Nota bene: in numpy l'istruzione A**k, non restituisce la potenza k di A intesa
#come prodotto scalare di A per se stessa k volte, ma si intende la matrice che si ottiene elevando a k 
#ciascun elemento della matrice A.
#Porre attenzione, osservando l'implementazione proposta

if M<1/5:
    print("La condizione è verificata, valore di M ",M)
    
    appinB=np.zeros((n,n))
    
    potA=I
    for k in range(0,4):
        appinB=appinB+potA
        potA=np.dot(potA,A)
    
    #calcolo l'errore relativo tra l'inversa calcolata con questa forma approssimata e l'inversa calcolata con
    #il metodo inv fi numpy.linalg
    errore1=npl.norm(appinB-invB,1)/npl.norm(invB,1)   
    print("Errore relativo calcolo inversa metodo potenze di A ",errore1)
  

#----PUNTO C : si dica se la matrice B assegnata ammette fattorizzazione LU senza pivoting;

#Verifico che la matrice B abbia i minori principali a rango massimo, ed in caso affermativo posso utilizzare
# il metodo di fattorizzazione di Gauss senza pivoting parziale  a perno massimo
    
det_minoreB=[]
for i in range (0,n):
    det_minoreB.append(npl.det(B[:i+1,:i+1]))
    
if np.all(det_minoreB!=0):
    print("La matrice B ammette fattorizzazione LU no-pivoting")
    
#----PUNTO D : se dal punto c) la sua esistenza è confermata, si calcoli la fattorizzazione LU di B senza pivoting; in
#   caso contrario si calcoli la fattorizzazione LU di B con pivoting parziale;

P,L,U,flag=LU_nopivot(B)

#Calcolo l'inversa della matrice B, risolvendo n sistemi lineari aventi come matrice dei coefficienti
#la matrice B e come termine noto le n colonne della matrice identità
if flag==0:
   X= solve_nsis_f(P,L,U,I)


#----PUNTO E : sfruttando la fattorizzazione calcolata al punto d) si costruisca l'inversa di B e la si confronti con
#   l'approssimazione ottenuta al punto b). Quale delle due risultera piu accurata?

#Calcolo l'errore relativo considerando come valore esatto dell'inversa quello calcolato dalla funzione inv di numpy.linalg
errore2=npl.norm(X-invB,1)/npl.norm(invB,1)
print("Errore relativo calcolo inversa metodo Soluzione n sistemi lineari ",errore2)

#Dal confronto dell'errore relativo commesso dai due metodi, considerando come valore esatto dell'inversa quello calcolato
#facendo uso della funzione inv del pacchetto numpy.linalg, si conclude che il metodo che sfrutta la fattorizzazione LU per
#calcolo dell'inversa e' più accurato rispetto al metodo della serie troncata