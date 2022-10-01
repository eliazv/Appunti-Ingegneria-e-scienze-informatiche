# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 08:29:40 2021

@author: damia
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#----------------------------PUNTO A-------------------------------------------
#si costruiscano, per i = 0;...; 5, le ordinate yi= 2/pi integrale da 0 a xi( 5.5(1-e^-0.05t)sen(t^2)) dt  utilizzando la formula di Simpson composita su Ni sottointervalli equispaziati in cui il valore di Ni
#è determinato automaticamente affinche il resto della formula di quadratura composita sia minore di tol = 1.e -8;

#[integrazioneNumerica]

#funzioni per l'integrazione Simposon Composita e con ricerca automatica del numero di N
#di sottointervalli
def SimpComp(fname,a,b,n):
    h=(b-a)/(2*n)
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[2:2*n:2])+4*np.sum(f[1:2*n:2])+f[2*n])*h/3
    return I



#----------------------------PUNTO B-------------------------------------------
#si costruisca il polinomio di interpolazione di Lagrange dei dati (xi; yi), i = 0; ... 5;

#interpolazioneLagrange

#Funzioni per l'interpolazione di Lagrange
def plagr(xnodi,k):
    """
    Restituisce i coefficienti del k-esimo pol di
    Lagrange associato ai punti del vettore xnodi
    """
    xzeri=np.zeros_like(xnodi)
    n=xnodi.size
    if k==0:
       xzeri=xnodi[1:n]
    else:
       xzeri=np.append(xnodi[0:k],xnodi[k+1:n])
    
    num=np.poly(xzeri) 
    den=np.polyval(num,xnodi[k])
    
    p=num/den
    
    return p


#----------------------------PUNTO C-------------------------------------------
#si rappresentino in uno stesso grafico i punti di interpolazione (xi; yi), i = 0; : : : ; 5 e il polinomio di
#interpolazione ottenuto al punto b);

def InterpL(x, f, xx):
     """"
        %funzione che determina in un insieme di punti il valore del polinomio
        %interpolante ottenuto dalla formula di Lagrange.
        % DATI INPUT
        %  x  vettore con i nodi dell'interpolazione
        %  f  vettore con i valori dei nodi 
        %  xx vettore con i punti in cui si vuole calcolare il polinomio
        % DATI OUTPUT
        %  y vettore contenente i valori assunti dal polinomio interpolante
        %
     """
     n=x.size
     m=xx.size
     L=np.zeros((n,m))
     for k in range(n):
        p=plagr(x,k)
        L[k,:]=np.polyval(p,xx)
    
    
     return np.dot(f,L)
 


#----------------------------PUNTO D?-------------------------------------------
#si dica quanti sottointervalli Ni sono stati necessari per il calcolo di ciascun yi, i = 0; : : : ; 5;
def simptoll(fun,a,b,tol):

    Nmax=4096
    err=1
    
    N=1;
    IN=SimpComp(fun,a,b,N);
    
    while N<=Nmax and err>tol :
        N=2*N
        I2N=SimpComp(fun,a,b,N)
        err=abs(IN-I2N)/15
        IN=I2N
 
    
    if N>Nmax:
        print('Raggiunto nmax di intervalli con simptoll')
        N=0
        IN=[]
 
    return IN,N



# Script principale

#punto A
tol=1e-08
x=np.zeros((6,))
y=np.zeros((6,))
N=np.zeros((6,))
fig=1

#Funzione integranda
f= lambda x: 2/math.pi*(5.5*(1-np.exp(-0.05*x))*np.sin(x**2))


for i in range(0,6):
    #Estremo destro dell'intervallo di integrazione
    x[i]=0.5+2*i
   
    #Costruisco punti nell'intervallo [0,x[i]] in cui valutare e poi disegnare la funzione integranda
    xi=np.linspace(0,x[i],100)
    plt.subplot(2,3,fig)
    plt.plot(xi,f(xi))
    plt.legend([ 'x['+str(i)+']='+str(x[i])])
    fig+=1
    #Calcolo il valore dell'integrale i-esimo  con a=0 e b= x[i]con la precisione richiesta
    y[i],N[i]=simptoll(f,0,x[i],tol)
 
plt.show()


#punto B
xx=np.linspace(min(x),max(x),100)
#Calcolo il polinomio che interpola le coppie (x,y)
pol=InterpL(x, y, xx)
#punto C
plt.plot(xx,pol,x,y,'ro')
plt.legend(['Polinomio interpolante','Nodi di interpolazione'])
plt.show()
#punto D
print("Numero di sottointervalli per ciascuni il calcolo di ciascun integrale \n",N)



#----------------------------PUNTO E-------------------------------------------
#si fornisca una spiegazione teorica alla risposta precedente.

"""
x= array([ 0.5, 2.5, 4.5, 6.5, 8.5, 10.5])

Valori degli integrali
Y= array([0.00269425, 0.00396974, 0.07267035, 0.09831532, 0.15747259, 0.15135967])

Numero di sottointervalli per il calcolo di ciascun integrale
[ 8. 128. 256. 512. 2048. 2048.]
Al variare di x[i], la funzione integranda ha un andamento sempre più oscillante.
Nella sua definizione c’è una funzione seno con argomento x**2 , la cui frequenza
aumenta all’aumentare dell’estremo destro dell’intervallo di integrazione x[i].
E quindi all’aumentare di x[i[ per ottenere la precisione richiesta per il calcolo 
dell’integrale è necessario un numero di suddivisioni maggiore.
"""