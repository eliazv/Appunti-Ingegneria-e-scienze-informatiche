# -*- coding: utf-8 -*-
"""
Ese1
"""

import numpy as np
import matplotlib.pyplot as plt
#from funzioni_zeri import newton_m, stima_ordine
import sympy as sym
from sympy.utilities.lambdify import lambdify
from scipy.optimize import fsolve


#----------------------------PUNTO A-------------------------------------------
#si stabilisca quante radici reali ha f nell'intervallo [5/6, 25/6] e si giustifichi la risposta;


x=sym.symbols('x')
fx= x-1/3*sym.sqrt(30*x-25)
dfx=sym.diff(fx,x,1)
print(dfx)

x0=4
f=lambdify(x,fx,np)
alfa=fsolve(f,x0)
print("La funzione ha uno zero in ", alfa)
fp=lambdify(x,dfx,np)
fp_alfa=fp(alfa)
print("La derivata prima  in ", alfa, 'vale ',fp_alfa)
x=np.linspace(5/6,25/6,100)
plt.plot(x,f(x))
plt.plot(x,[0]*100)
plt.plot(alfa,0,'ro')
plt.show()


#In alfa=1.66666667 si annula sia la funzione che la sua derivata prima,
#la funzione ha in x=1.66666667 uno xero con molteplicita=2 
m=2
tolx=1e-12
tolf=1e-12
nmax=100



#----------------------------PUNTO B-------------------------------------------
#si costruisca un metodo iterativo che, partendo da x(0) = 4, converga ad alpha (zero di f), quadraticamente;

def newton_m(fname,fpname,x0,m,tolx,tolf,nmax):
        eps=np.spacing(1)     
        xk=[]
        #xk.append(x0)
        fx0=fname(x0)
        dfx0=fpname(x0)
        if abs(dfx0)>eps:
            d=fx0/dfx0
            x1=x0-m*d
            fx1=fname(x1)
            xk.append(x1)
            it=0
           
        else:
            print('Newton:  Derivata nulla in x0  \n')
            return [],0,[]
        
        it=1
        while it<nmax and abs(fx1)>=tolf and  abs(d)>=tolx*abs(x1):
            x0=x1
            fx0=fname(x0)
            dfx0=fpname(x0)
            if abs(dfx0)>eps:
                d=fx0/dfx0
                x1=x0-m*d
                fx1=fname(x1)
                xk.append(x1)
                it=it+1
            else:
                 print('Newton Mod: Derivata nulla   \n')
                 return x1,it,xk           
           
        if it==nmax:
            print('Newton Mod: raggiunto massimo numero di iterazioni \n');
        
        return x1,it,xk

#Metodo iterativo che converge quadraticamente al alfa: metodo di Newton Modificato con m=2
x1,it,xk= newton_m(f,fp,x0,m,tolx,tolf,nmax)




#----------------------------PUNTO C-------------------------------------------
     #si verifichi numericamente l'ordine di convergenza del metodo implementato al punto b);   

def stima_ordine(xk,it):
    p=[]

    #Fa un ciclo prendendo gli ultimi 3 valori della successione di iterati.
    for k in range(it-3): 
        num = np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))
        den = np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1]))
        p.append(num/den);
   
    ordine=p[-1]
    return ordine


#Verifico l'ordine di convergenza
ordine=stima_ordine(xk,it)



#----------------------------PUNTO D-------------------------------------------
    #si rappresenti in un grafico in scala semilogaritmica sulle y ecc...

plt.plot(range(it),np.abs(xk))
plt.show()



#----------------------------PUNTO E-------------------------------------------
    # b puo convergere ad quadraticamente anche alpha partendo dall'estremo sinistro dell'intervallo

#Il metodo non converge se scelgo come iterato iniziale x0=5/6,
#perchè la derivata prima in  5/6 diverge  va a -infinito