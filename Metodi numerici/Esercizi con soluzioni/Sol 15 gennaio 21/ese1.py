# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:09:59 2021

@author: damia
"""

import numpy as np
import matplotlib.pyplot as plt
from funzioni_zeri import iterazione
import sympy as sym
from sympy.utilities.lambdify import lambdify

#PUNTO A : dopo aver implementato la successione ui=1;:::;35 con la formula ricorrente (2), si osserva che tutti
#gli ui calcolati dalla (2) coincidono con i valori in (1), e la successione converge eettivamente a 5;

n=35
u1=np.zeros((n,),dtype=float)
u2=np.zeros((n,),dtype=float)
u3=np.zeros((n,),dtype=float)


for i in range(1,n+1):
    u1[i-1]=15*((3/5)**(i)+1)/(5*(3/5)**(i)+3)

u2[0]=4
for i in range(1,n):
    u2[i]=8-15/u2[i-1]


u3[0]=4
u3[1]=17/4
for i in range(3,n+1):
    u3[i-1]=108-815/u3[i-2]+1500/(u3[i-2]*u3[i-3])

plt.plot(range(n),u1)
plt.title('Formula 1')
plt.show()

plt.plot(range(n),u2)
plt.title('Formula 2')
plt.show()

#I due grafici sono uguali, i valori di 1 e 2 coincidono


#PUNTO B : dopo aver implementato la successione fuigi=1;:::;35 con la formula ricorrente (3), si osserva che, al
#crescere di i, gli ui calcolati dalla (3) si discostano sempre piu dai valori deniti dalla (1), e la
#successione converge a 100 anziche a 5;
plt.plot(range(n),u3)
plt.title('Formula 3')
plt.show()

#PUNTO C : al variare di i nel range 1 <= i <= 35, si mostrano in un graco in scala semilogaritmica sulle y gli errori
#relativi generati dalle formule ricorrenti a due e a tre termini in (2) e (3), utilizzando come valori esatti
#degli ui quelli dati dalla formula (1);
err_rel2=np.abs(u2-u1)/np.abs(u1)
err_rel3=np.abs(u3-u1)/np.abs(u1)

plt.semilogy(range(n),err_rel2,  range(n),err_rel3)
plt.legend(['Errore relativo formula 2', 'Errore relativo formula 3'])
plt.show()



g1=lambda x:  8-15/x

g2=lambda x:  108-815/x+ 1500/(x**2);

x=sym.symbols('x')

#Definisco funzione g1
g1x= 8-15/x
dg1x=sym.diff(g1x,x,1)
dg1=lambdify(x,dg1x,np)
g1=lambdify(x,g1x,np)


#Definisco funzione g2
g2x=108-815/x+1500/(x**2)
dg2x=sym.diff(g2x,x,1)
dg2=lambdify(x,dg2x,np)
g2=lambdify(x,g2x,np)

 
x=np.linspace(4,100 ,100)
plt.plot(x,g1(x))
plt.plot(x,x)
plt.legend(['g1(x)','y=x'])
plt.show()

#La g2 interseca la bisettrice in 2 punti, ha due punti fissi (x=5 ed 100) , ma la derivata prima della g2
# non soddisfa le ipotesi del teorema di convergenza locale in un intorno del primo punto fisso,5
plt.plot(x,g2(x))
plt.plot(x,x)
plt.legend(['g2(x)','y=x'])
plt.show()
 
tolx=1e-5
nmax=100
x0=4
x1,xk,it=iterazione(g1,x0,tolx,nmax)
x2,xk2,it2=iterazione(g2,x0,tolx,nmax)
print("Punto fisso della funzione g1 -->  ",x1)
print("Punto fisso della funzione g1 -->  ",x2)

#Visualizziamo la derivata prima di g1 in un intorno di 5, sono soddisfatte le iptesi del teorema di convergenza
#locale
xx=np.linspace(2,6,100)
plt.semilogy(xx,dg1(xx))
plt.plot([2,6],[1,1])
plt.plot([2,6],[-1,-1])
plt.legend(['derivata prima di g1 in un intorno di 5 ', 'y=1','y=-1'])
plt.show()
xx=np.linspace(2,6,100)
plt.semilogy(xx,dg2(xx))
plt.plot([2,6],[1,1])
plt.plot([2,6],[-1,-1])
plt.legend(['derivata prima di g2 in un intorno di 5 ', 'y=1','y=-1'])
 
    
plt.show()

xx=np.linspace(95,105,100)
plt.plot(xx,dg2(xx))
plt.plot([95,105],[1,1])
plt.plot([95,105],[-1,-1])
 
plt.legend(['Derivata prima  di g2 in un intorno di 100','y=1','y=-1'])
  

