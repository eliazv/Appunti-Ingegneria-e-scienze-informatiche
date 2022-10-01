# -*- coding: utf-8 -*-
"""
ese2
"""

import numpy as np
from funzioni_Interpolazione_Polinomiale import InterpL,plagr
import matplotlib.pyplot as plt
import math

#PUNTO A : si determinano i due polinomi di interpolazione di grado n = 5 : 5 : 30 della funzione
#f (rispettivamente detti p(e)n(x) e p(c)n(x) ) che si ottengono dalla formula di Newton
#sui nodi equispaziati xi^e= ... i = 1; :::; n + 1 e sui nodi di Chebyshev xi^c=...
def zeri_Cheb(n):
    x=np.zeros((n+1,))
    for k in range(n+1):
        x[k]=np.cos(((2*k+1)/(2*(n+1))*math.pi))

    return x
                          
                          
                          
                          
f= lambda x: 1/(1+900*x**2)


a=-1
b=1;
 
 
xx=np.linspace(a,b,200);


#PUNTO B : dopo aver creato la Figura 1 e suddiviso la finestra grafica in 2 x 3 sottofinestre, si
#disegnano nelle 6 sottofinestre i grafici di r(e)(x) = |f(x) - p(e)n (x)|, x appartenete a [-1; 1] al variare di n;
fig=1
Le=np.zeros((200,1));
for n in range(5,35,5):
    xe=np.linspace(a,b,n+1)
     

    ye=f(xe)
    pole=InterpL(xe,ye,xx);
    re=np.abs(f(xx)-pole)
    
    #il metodo subplot_adjust serve per spaziare meglio visivamente i grafici della tabella
    plt.subplots_adjust(hspace=0.5,wspace=0.5)
    plt.subplot(3,2,fig)
    
    plt.plot(xx,np.abs(f(xx)-pole))
    plt.legend(['Equidistanti n='+str(n)])
    #plt.subplot(3,2,fig)
    
    fig+=1
plt.show()
    
   
 
#PUNTO C : dopo aver creato la Figura 2 e suddiviso la finestra grafica in 2 x 3 sottofinestre, si
#disegnano nelle 6 sottofinestre i grafici di r(c)(x) = |f(x) - p(c)n (x)|, x appartenete a [-1; 1] al variare di n; 
fig=1
for n in range(5,35,5):
    
    xc=zeri_Cheb(n)

    yc=f(xc)
    polc=InterpL(xc,yc,xx);
    rc=np.abs(f(xx)-polc)
    plt.subplots_adjust(hspace=0.5,wspace=0.5)  
    plt.subplot(3,2,fig)
    
    plt.plot(xx,rc)
    plt.legend(['Cheb'+str(n)])
    fig+=1
plt.show()
    


#PUNTO D : si calcolano le approssimazioni della costante di Lebesgue sia nel caso di nodi equi-
#spaziati che di Chebyshev, e si rappresentano in un grafico in scala semilogaritmica
#su y (comando semilogy eventualmente preceduto da set(gca,'yscale','log')) al va-
#riare di n (Figura 3).

#Calcolo delle costanti di Lebesgue per ogni n
LLe=np.zeros((6,1));
LLc=np.zeros((6,1));
Lc=np.zeros((200,1))
Le=np.zeros((200,1))

i=0;
for n in range(5,35,5):

    #nodi equispaziati
    xe=np.linspace(a,b,n+1)
    #nodi di Chebyshev 
    xc=zeri_Cheb(n)
    
    Le=np.zeros((200,1));
    Lc=np.zeros((200,1));
    for l in range (n+1):        
        pe=plagr(xe,l);
        Le=Le+np.abs(np.polyval(pe,xx))
        pc=plagr(xc,l)
        Lc=Lc+np.abs(np.polyval(pc,xx))
    
    LLe[i]=np.max(Le)
    LLc[i]=np.max(Lc)
    i=i+1

plt.semilogy(range(5,35,5),LLe, range(5,35,5),LLc)
plt.legend(['Caso nodi equisistanti','Caso zeri di Chebichev'])
plt.title('Costanti di lebesgue:')
plt.show()