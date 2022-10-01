# -*- coding: utf-8 -*-
"""
esercizio 2
"""

import numpy as np
import sympy as sym
import funzioni_zeri
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify
from scipy.optimize import fsolve
tolx=1e-7
nmax=1000

 
f= lambda x: np.exp(x)-4*x**2

#----PUNTO A : si rappresenti la funzione f sull'intervallo assegnato, si dica quanti zeri reali possiede e in quali intervalli
#   interi dell'asse reale sono localizzati;

#Disegno la funzione nell'intervallo assegnato
xx=np.linspace(-1.0,5.0,100)
plt.plot(xx,0*xx,xx,f(xx))
plt.show()
#La funzione ha tre zeri, uno nell'intervallo [-0.8,0], il secondo nell'intervallo [0,1] ed il terzo nell'intervallo[4,5]
#Utilizzo il metodo fsolve di scipy.optimize per calcolare ciascuno degli zeri alfa_i della funzione f,
#prende in input l'iterato iniziale x0

x0=-0.8
alfa0=fsolve(f, x0)
print("Lo zero della funzione e' ",alfa0)
x0=0.5
alfa1=fsolve(f, x0)
print("Lo zero della funzione e' ",alfa1)
x0=4.0
alfa2=fsolve(f, x0)
print("Lo zero della funzione e' ",alfa2)
#Disegno: l'asse x e la funzione f valutata in un intervallo opportuno
xx=np.linspace(-1.0,5.0,100)
plt.plot(xx,0*xx,xx,f(xx),alfa0,0,'ro',alfa1,0,'bo',alfa2,0,'go')
plt.legend(['Asse x','Funzione f', 'zeri'])
plt.show()

#----PUNTO B : si dica se il procedimento iterativo ... puo potenzialmente essere utilizzato per
#   determinare tutte le radici di f oppure no, motivando opportunamente la risposta;

'''
Definisco la funzione g in formato simbolico perchè poi utilizzo la funzione diff
di sympy per calcolare l'espressione analitica della derivata prima'
'''
x=sym.symbols('x')

#Considero la funzione g indicata dalla traccia del compito
gx=0.5*sym.exp(x/2)

#Disegno la funzione g(x) e la bisettrice y=x
g=lambdify(x,gx,np)
plt.plot(xx,xx,xx,g(xx),alfa0,alfa0,'ro',alfa1,alfa1,'bo',alfa2,alfa2,'go')
plt.title('funzione g(x) e y=x')
plt.show()

#Dal grafico osservo che la funzione g proposta dall'esercizio può potenzialmente essere utilizzata
#per calcolare solamente  la seconda e la terza radice, poichè la g non interseca la bisettrice nella radice alfa1.

#Calcolo la derivata prima di gx espressione simbolica tramite la funzione diff del modulo sym 
dgx=sym.diff(gx,x,1)


dg=lambdify(x,dgx,np)

#Disegno la funzione dg(x) 

#Posso giustifcare la convergenza del procedimento iterativo guardando la derivata prima di g(x)
#in un intorno della soluzione: il metodo genera una successione di iterati convergenti alla radice alfa
# ed appartenenti a questo intorno se |g'(x)|< 1 in un intorno della soluzione

 
plt.plot(xx ,dg(xx ))
plt.plot(alfa1,0,'bo',alfa2,0,'go')
#Disegno la retta y=1
plt.plot([-1,5],[1,1],'--')
#Disegno la retta y=-1
plt.plot([-1,5],[-1,-1],'--')
plt.title('funzione dg(x) proposta dalla traccia ')
 
plt.legend(['Grafico derivata prima di g1 (x)', 'Zero','Zero' ,'Retta y=1', 'Retta y=-1'])
plt.show()

#Dal grafico vedo che per la funzione g proposta dalla traccia
# le ipotesi del teorema di convergenza locale sono soddisfatte solo in un intorno della seconda soluzione,
#mentre non vengono soddisfatte per la terza soluzione,
#perchè nell'intorno della soluzion3 4.3065 non risulta che |g'(x) |<1


#----PUNTO C : si implementi il metodo di punto fisso che utilizza la funzione di iterazione g(x) indicata al punto b);

def iterazioneAPuntoFisso(g,x0,tolx,itmax):
    xk=[]
    xk.append(x0)
    x1=g(x0) #La nuova x è la x0 calcolata nella funzione g(x)
    d=x1-x0
    xk.append(x1)
    it=1
    while it <= itmax and  abs(d)>=tolx*abs(x1) :
        x0=x1
        x1=g(x0) #La nuova x è la x0 calcolata nella funzione g(x)
        d=x1-x0 #Differenza tra le due iterate per la CONDIZIONE di ARRESTO
        it=it+1 #Incremento l'iterata
        xk.append(x1)

    #aggiunto
    if it == itmax:
        print("massimo numero di iterazioni raggiunto")
  
    return   x1, it, xk

#----PUNTO D : si scelgano i valori iniziali x(0) = 0:5 e x(0) = 4:5, e si verifichi se il metodo di punto fisso risulta essere
#    convergente in entrambi i casi oppure no, motivando la risposta;

#----PUNTO E : per le scelte di x(0) in cui si ha convergenza si rappresenti in un grafico il valore dell'approssimazione x(k)
#   ottenuta al variare di k  0 e si calcoli l'ordine di convergenza del metodo iterativo.

#Utilizzo il metodo di iterazione funzionale per calcolare il punto fisso di g a partire da x0=0.5
#Mi aspetto la convergenza del metodo
x0=0.5
x1,it,xk=funzioni_zeri.iterazione(g,x0,tolx,nmax)
print('iterazioni= {:d}, soluzione={:e} \n\n'.format(it,x1))
#Calcolo l'ordine del metodo
ordine_iter= funzioni_zeri.stima_ordine(xk,it)
#Essendo il metodo con ordine di convergenza lineare, la costante asintotica di convergenza è data
#da |g'(alfa)| dove alfa è la radice.

 
print("x0=0.5, Soluzione {:e} Iterazioni it={:d}, ordine di convergenza {:e}".format(x1,it,ordine_iter ))

plt.plot(range(it+1),xk)
plt.xlabel('iterazioni')
plt.ylabel('xk')

#Utilizzo il metodo di iterazione funzionale per calcolare il punto fisso di g  a partire da x0=4.5
#Mi aspetto che il metodo non converga
x0=4.5
x1,it,xk=funzioni_zeri.iterazione(g,x0,tolx,nmax)
print('x0=4.5, Soluzione {:e} iterazioni= {:d}, Il metodo non converge\n\n'.format(x1,it))



 

