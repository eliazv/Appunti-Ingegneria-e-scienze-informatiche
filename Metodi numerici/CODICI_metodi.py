# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:26:07 2021

@author: Elia
"""
import numpy as np
import scipy.linalg as spl
import matplotlib.pyplot as plt
import math
import sympy as sym
from sympy.utilities.lambdify import lambdify
from scipy.optimize import fsolve
import numpy.linalg as npl
from scipy.fft import fft #fourier



#---------------Approssimazione Minimi Quadrati-----------------
"""
    INPUT
    xnodi vettore colonna con le ascisse dei punti
    ynodi vettore colonna con le ordinate dei punti 
    n grado del polinomio approssimante
    OUTPUT
     a vettore colonna contenente i coefficienti incogniti
 """
def MetodoQR(xnodi,ynodi,n):
    H=np.vander(xnodi,n+1)
    Q,R=spl.qr(H)
    y1=np.dot(Q.T,ynodi)
    A,flag=U_solve(R[0:n+1,:],y1[0:n+1])
    return  A




#---------------------FattorizzazioneLU----------------------

#function che implementa il metodo delle sostituzioni IN AVANTI per risolvere un sistema
#lineare con matrice dei coecienti triangolare inferiore.
def Lsolve(L,b):
    """  
    Risoluzione con procedura forward di Lx=b con L triangolare inferiore  
     Input: L matrice triangolare inferiore
            b termine noto
    Output: x: soluzione del sistema lineare
            flag=  0, se sono soddisfatti i test di applicabilità
                   1, se non sono soddisfatti
    """
#test dimensione
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


#function che implementa il metodo delle sostituzioni ALL'INDIETRO per risolvere un sistema
#lineare con matrice dei coefficienti triangolare superiore.
def Usolve(U,b):
    
    """
    Risoluzione con procedura backward di Rx=b con R triangolare superiore  
     Input: U matrice triangolare superiore
            b termine noto
    Output: x: soluzione del sistema lineare
            flag=  0, se sono soddisfatti i test di applicabilità
                   1, se non sono soddisfatti
    
    """ 
#test dimensione
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




def LUsolve(L,U,P,b):
     """
     Risoluzione a partire da PA =LU assegnata
     """
     Pb=np.dot(P,b)
     y,flag=Lsolve(L,Pb)
     if flag == 0:
         x,flag=Usolve(U,y)
     else:
        return [],flag

     return x,flag
 
#LUnopivot.m    
#restituisce in output le matrici L e U associate al metodo di eliminazione gaussiana senza pivoting.
def LU_nopivot(A):
    """
    % Fattorizzazione PA=LU senza pivot   versione vettorizzata
    In output:
    L matrice triangolare inferiore
    U matrice triangolare superiore
    P matrice identità
    tali che  LU=PA=A
    """
    # Test dimensione
    m,n=A.shape
   
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag
  
    P=np.eye(n);
    U=A.copy();
 # Fattorizzazione
    for k in range(n-1):
       #Test pivot 
          if U[k,k]==0:
            print('elemento diagonale nullo')
            L,U,P,flag=[],[],[],1 
            return P,L,U,flag

  #     Eliminazione gaussiana
          U[k+1:n,k]=U[k+1:n,k]/U[k,k]                                   # Memorizza i moltiplicatori	  
          U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n])  # Eliminazione gaussiana sulla matrice
     
  
    L=np.tril(U,-1)+np.eye(n)  # Estrae i moltiplicatori 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,flag


def LU_nopivotv(A):
    """
    % Fattorizzazione PA=LU senza pivot   versione vettorizzata intermedia
    In output:
    L matrice triangolare inferiore
    U matrice triangolare superiore
    P matrice identità
    tali che  LU=PA=A
    """
    # Test dimensione
    m,n=A.shape
   
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag
  
    P=np.eye(n);
    U=A.copy();
 # Fattorizzazione
    for k in range(n-1):
       #Test pivot 
          if U[k,k]==0:
            print('elemento diagonale nullo')
            L,U,P,flag=[],[],[],1 
            return P,L,U,flag

  #     Eliminazione gaussiana
          for i in range(k+1,n):
             U[i,k]=U[i,k]/U[k,k]                                   # Memorizza i moltiplicatori	  
             U[i,k+1:n]=U[i,k+1:n]-U[i,k]*U[k,k+1:n]  # Eliminazione gaussiana sulla matrice
     
  
    L=np.tril(U,-1)+np.eye(n)  # Estrae i moltiplicatori 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,flag


def LU_nopivotb(A):
    """
    % Fattorizzazione PA=LU senza pivot  versione base
    In output:
    L matrice triangolare inferiore
    U matrice triangolare superiore
    P matrice identità
    tali che  LU=PA=A
    """
    # Test dimensione
    m,n=A.shape
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag
  
    P=np.eye(n);
    U=A.copy();
 # Fattorizzazione
    for k in range(n-1):
         #Test pivot 
         
         
          if U[k,k]==0:
            print('elemento diagonale nullo')
            L,U,P,flag=[],[],[],1 
            return P,L,U,flag

  #     Eliminazione gaussiana
          for i in range(k+1,n):
                U[i,k]=U[i,k]/U[k,k]
                for j in range(k+1,n):                                 # Memorizza i moltiplicatori	  
                  U[i,j]=U[i,j]-U[i,k]*U[k,j]  # Eliminazione gaussiana sulla matrice
     
  
    L=np.tril(U,-1)+np.eye(n)  # Estrae i moltiplicatori 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,flag


#di digi
def  LULUsolve(L,U,c):
    #Soluzione del sistema lineare A**2 x= c che equivale a L U L U x =c
    """  
    Conviene utilizzare la strategia proposta , perchè se la matrice A è mal condizionata, 
    il sistema lineare con matrice A**2 ha un indice di condizionamento dell'ordine del suo
    quadrato, quindi conviene risolvere i 4 sistemi lineari con matrici triangolari che hanno 
    indice di condizionamento sicuramente minore di A**2
    """ 
    y3,flag=Lsolve(L,c)
    y2,flag=Usolve(U,y3)
    y1,flag=Lsolve(L,y2)
    x,flag=Usolve(U,y1)
    return x


def swapRows(A,k,p):
    A[[k,p],:] = A[[p,k],:]
    
    
def LU_pivot(A):
    """
    % Fattorizzazione PA=LU con pivot 
    In output:
    L matrice triangolare inferiore
    U matrice triangolare superiore
    P matrice di permutazione
    tali che  PA=LU
    """
    # Test dimensione
    m,n=A.shape
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag
  
    P=np.eye(n);
    U=A.copy();
 # Fattorizzazione
    for k in range(n-1):
       #Scambio di righe nella matrice U e corrispondente scambio nella matrice di permutazione per
       # tenere traccia degli scambi avvenuti
       
       #Fissata la colonna k-esima calcolo l'indice di riga p a cui appartiene l'elemento di modulo massimo a partire dalla riga k-esima
          p = np.argmax(abs(U[k:n,k])) + k
          if p != k:
              swapRows(P,k,p)
              swapRows(U,k,p)

  #     Eliminazione gaussiana
          U[k+1:n,k]=U[k+1:n,k]/U[k,k]                                   # Memorizza i moltiplicatori	  
          U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n])  # Eliminazione gaussiana sulla matrice
     
  
    L=np.tril(U,-1)+np.eye(n)  # Estrae i moltiplicatori 
    U=np.triu(U)           # Estrae la parte triangolare superiore + diagonale
    return P,L,U,flag



def solve_nsis(A,B):
  # Test dimensione  
    m,n=A.shape
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
       
      return
    
    Y= np.zeros((n,n))
    X= np.zeros((n,n))
    P,L,U,flag= LU_nopivot(A)   #oppure passiamo P L U B negli argomenti
    
    if flag==0:
        for i in range(n):
            y,flag=Lsolve(L,np.dot(P,B[:,i]))
            Y[:,i]=y.squeeze(1)
            x,flag= Usolve(U,Y[:,i])
            X[:,i]=x.squeeze(1)
    else:
        print("Elemento diagonale nullo")
        X=[]
    return X    


#Uguale a quella precedente  
def solve_nsis_f(P,L,U,B):
  # Test dimensione  
    m,n=L.shape
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
       
      return
    
    Y= np.zeros((n,n))
    X= np.zeros((n,n))
  
    
    if flag==0:
        for i in range(n):
            y,flag=Lsolve(L,np.dot(P,B[:,i]))
            Y[:,i]=y.squeeze(1)
            x,flag= Usolve(U,Y[:,i])
            X[:,i]=x.squeeze(1)
    else:
        print("Elemento diagonale nullo")
        X=[]
    return X    





#---------------------Integrazione Numerica----------------------

def TrapComp(f, a, b, n):
    h = (b-a)/n
    x = np.arange(a, b+h, h)    # x = nodi
    y = f(x)
    I = (y[0] + 2*np.sum(y[1:n]) + y[n])*(h/2)
    return I


# Stima del numero N si sottointervalli per approssimare l'integrale della
# funzione integranda con precisione tol
def TrapToll(f, a, b, toll):
    nMax = 2048
    n = 1
    err = 1
    In = TrapComp(f, a, b, n)
    while n <= nMax and err > toll:
        n = n*2
        I2n = TrapComp(f, a, b, n)  #trapezi
        err = abs(I2n - In)/3
        In = I2n
        
    if n>nMax:
        print('Raggiunto nmax di intervalli con traptoll')
        n=0
        In=[]
 
    return In,n


#formula di Simpson Composita : 
def SimpComp(f, a, b, n):
    h = (b-a)/(n*2)
    x = np.arange(a, b+h, h)
    y = f(x)
    I = (y[0] + 2*np.sum(y[2:n*2:2]) + 4*np.sum(y[1:n*2:2]) + y[n])*(h/3)
    return I

#formula di Simpson Composita rispetto alla tolleranza :
# ricerca automatica del numero di N di sottointervalli
def SimpToll(f, a, b, toll):
    nMax = 2048
    n = 1
    err = 1
    In=SimpComp(f,a,b,n);   #In = TrapComp(f, a, b, n) in altri esercizi    
    while n <= nMax and err > toll:
        n = n*2
        I2n = SimpComp(f, a, b, n)
        err = abs(I2n - In)/15
        In = I2n
        
    if N>Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        n=0
        In=[]
 
    return In,n     #In sarebbe ~I e n sarebbe il numero di suddivisioni





    
#---------------------Interpolazione Lagrange----------------------


# Restituisce i coefficienti del k-esimo pol di Lagrange associato ai punti del vettore xnodi
def PLagr(xnodi, k):

    xzeri=np.zeros_like(xnodi) #aggiunta
    n=xnodi.size  #aggiunta 

    if k==0:
       xzeri=xnodi[1:n]
    else:
       xzeri=np.append(xnodi[0:k],xnodi[k+1:n])
    
    num=np.poly(xzeri) #trova i coefficienti di un polinomio avente quella determinata sequenza di zeri
    den=np.polyval(num,xnodi[k]) #valuta il polinomio nello specifico valore xnodi[k]
    
    return num/den



def InterpL(xnodi, ynodi, xx):
     """
        %funzione che determina in un insieme di punti il valore del polinomio
        %interpolante ottenuto dalla formula di Lagrange.
        % DATI INPUT
        %  xnodi  vettore con i nodi dell'interpolazione
        %  ynodi  vettore con i valori dei nodi 
        %  xx vettore con i punti in cui si vuole calcolare il polinomio
        % DATI OUTPUT
        %  y vettore contenente i valori assunti dal polinomio interpolante
        %
     """
     r=xnodi.size
     c=xx.size
     L=np.zeros((r,c))
     #calcolo tanti polinomi di lagrange quanti sono i nodi dell'interpolazione
     for k in range(r):
        p=PLagr(xnodi,k)
        L[k]=np.polyval(p,xx) #valuto il polinomio di lagrange di grado k nei valori xx
    
     return np.dot(ynodi, L)
 
    
    
f = lambda x : np.cos(np.pi * x) + np.sin(np.pi * x)
xx = np.linspace(0, 2, 100)
nodi = np.array([0.25, 0.75, 1, 1.5, 1.75])
plag = InterpL(nodi, f(nodi), xx)

plt.plot(xx, f(xx), "-r")
plt.plot(nodi, f(nodi), "x")
plt.plot(xx, plag, "-b")
plt.show()


#non so se utile
#La funzione fpol è la funzione che valuta il polinomio interpolatore
# in un numpy array val
def fpol(val):
    pol=InterpL(x,y,val)    
    return pol 




#------------------------Zeri di Funzione--------------------------

def concordi(x1, x2):
    return math.copysign(1, x1) == math.copysign(1, x2)


def bisez(fname,a,b,tol):
    eps=np.spacing(1)    #np.spacing(1) restituisce l'eps di macchina.
    fa=fname(a)
    fb=fname(b)
    if sign(fa)==sign(fb):
       print('intervallo non corretto --Metodo non applicabile')
       return [],0,[]
    else:
        maxit=int(math.ceil(math.log((b-a)/tol)/math.log(2))) #numero massimo di iterazioni
        print('n. di passi necessari=',maxit,'\n');
        xk=[]
        it=0
        while it<maxit and  abs(b-a)>=tol+eps*max(abs(a),abs(b)):
            c=a+(b-a)*0.5   #formula stabile per il calcolo del punto medio dell'intervallo
            xk.append(c) 
            it+=1
            fxk=fname(c) 
            if fxk==0:
                break
            elif sign(fxk)==sign(fa):
                a=c
                fa=fxk
            elif sign(fxk)==sign(fb):
                b=c
                fb=fxk     
        x=c
        
    return x,it,xk


def regula_falsi(fname,a,b,tol,nmax):    
    eps=np.spacing(1)
    xk=[]
    fa=fname(a)
    fb=fname(b)
    if sign(fa)==sign(fb):
        print('intervallo non corretto --Metodo non applicabile')
        return [],0,[]
    else:
        it=0
        fxk=fname(a)
        while it<nmax and  abs(b-a)>=tol+eps*max(abs(a),abs(b)) and abs(fxk)>=tol :
            x1=a-fa*(b-a)/(fb-fa); #
            xk.append(x1)
            fxk=fname(x1);
            if fxk==0:
                break
            elif sign(fxk)==sign(fa):
                a=x1;
                fa=fxk;
            elif sign(fxk)==sign(fb):
                b=x1;
                fb=fxk;
            it+=1
                
        if it==nmax :
            print('Regula Falsi: Raggiunto numero max di iterazioni')
       
    return x1,it,xk



def corde(fname,fpname,x0,tolx,tolf,nmax):
 #Corde
        xk=[]
        m=fpname(x0)               #m= Coefficiente angolare della tangente in x0, è costante
        fx0=fname(x0)
        d=fx0/m
        x1=x0-d
        fx1=fname(x1)
        xk.append(x1)
        it=1
        while it<nmax and  abs(fx1)>=tolf and abs(d)>=tolx*abs(x1) :
           x0=x1
           fx0=fname(x0)
           d=fx0/m
           '''
           #x1= ascissa del punto di intersezione tra  la retta che passa per il punto
           (xi,f(xi)) e ha pendenza uguale a m  e l'asse x
           '''
           x1=x0-d  
           fx1=fname(x1)
           it=it+1
           xk.append(x1)
          
        if it==nmax:
            print('raggiunto massimo numero di iterazioni \n')
            
        
        return x1,it,xk


def secanti(fname,xm1,x0,tolx,tolf,nmax):#necessarie due interate iniziali
        xk=[]
        fxm1=fname(xm1);
        fx0=fname(x0); 
        d=fx0*(x0-xm1)/(fx0-fxm1)
        x1=x0-d;
        xk.append(x1)
        fx1=fname(x1);
        it=1
       
        while it<nmax and abs(fx1)>=tolf and abs(d)>=tolx*abs(x1):
            xm1=x0
            x0=x1
            fxm1=fname(xm1)
            fx0=fname(x0) 
            d=fx0*(x0-xm1)/(fx0-fxm1)
            x1=x0-d
            fx1=fname(x1)
            xk.append(x1);
            it=it+1;
           
       
        if it==nmax:
           print('Secanti: raggiunto massimo numero di iterazioni \n')
        
        return x1,it,xk
    
    
#convergenza quadratica
def newton(fname,fpname,x0,tolx,tolf,nmax):
#Newton
        xk=[]
        fx0=fname(x0)
        dfx0=fpname(x0)
        if abs(dfx0)>np.spacing(1):
            d=fx0/dfx0
            x1=x0-d
            fx1=fname(x1)
            xk.append(x1)
            it=0
           
        else:
            print('Newton:  Derivata nulla in x0 - EXIT \n')
            return [],0,[]
        
        it=1
        while it<nmax and abs(fx1)>=tolf and  abs(d)>=tolx*abs(x1):
            x0=x1
            fx0=fname(x0)
            dfx0=fpname(x0)
            if abs(dfx0)>np.spacing(1):
                d=fx0/dfx0
                x1=x0-d
                fx1=fname(x1)
                xk.append(x1)
                it=it+1
            else:
                 print('Newton: Derivata nulla in x0 - EXIT \n')
                 return x1,it,xk           
           
        if it==nmax:
            print('Newton: raggiunto massimo numero di iterazioni \n');
        
        return x1,it,xk

#Newton modificato
#l’ordine di convergenza del metodo è 2.
#da utilizzare quando anche la derivata della radice è zero.
"""
fname : labdify di fx
fpname : labdify di derivata
x0
m=2
tolx, tolf = 1e-12
nmax=100
"""
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



"""
inputs: funzione di iterazione, approssimazione iniziale, tolleranza e numero massimo di iterazioni.
outputs: la soluzione sol dell'equazione non lineare, il numero di iterazioni compiute iter e il vettore delle approssimazioni xk.
"""
def iterazioneAPuntoFisso(g,x0,tolx,itmax):     #metodoIterativoAPuntoFisso
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


"""
Per verificare numericamente l'ordine di convergenza (stimaConvergenza).
Ha bisogno di 3 valori per questo calcolo xk xk-1 e xk-2, in particolare degli ultimi 3 che sono stati iterati.
"""
def stima_ordine(xk,it):
    p=[]

    #Fa un ciclo prendendo gli ultimi 3 valori della successione di iterati.
    for k in range(it-3): 
        num = np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))
        den = np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1]))
        p.append(num/den);
   
    ordine=p[-1]
    return ordine






#-----------------------------------------------Fourier--------------------------------------------------

"""
TrasformataDiFourierES1)
Scrivere uno script che calcoli il polinomio trigonometrico di un opportuno grado
m che interpoli un insieme di punti Pi = (xi; yi), i = 0; :::; n, con xi punti
equidistanti in un intervallo [a,b) e yi = f(xi) ottenuti dalla valutazione nei
punti xi di una funzione test f : [a; b] -> R. Testare lo script sulle funzioni

• f(x) = sin(x) - 2 sin(2x), x appartenete [-pi; pi),
• f(x) = sinh(x), x appartenete [-2; 2),
• f(x) = |x|, x appartenete [-1; 1),
• f(x) = 1/(1 + x^2), x appartenete [-5; 5) (funzione di Runge).

Calcolare l'errore di interpolazione r(x) = f(x)-p(x), tra la funzione test
f(x) e il polinomio di interpolazione p(x). Visualizzare il grafico di f(x)
e p(x), ed il grafico di jr(x)j. Cosa si osserva? Cosa accade all'aumentare
del grado n di p(x)?
"""
A = -3
B = 3

n=int(input("n = "))
step = (B-A)/(n+1)
xx = np.arange(A, B, step)
y = []

i = 0
for xi in xx:
    if xi <= -1 or xi > 1:    
        y.append(1)
    else:
        y.append(0)
    i = i+1
    
m = n//2
l, r = 0, 2*math.pi
c = fft(y)
a = np.zeros((m+2, ))
b = np.zeros((m+2, ))

a0 = c[0]/(n+1)
a[1:m+1] = 2*c[1:m+1].real/(n+1)
b[1:m+1] = -2*c[1:m+1].imag/(n+1)

if n%2 != 0:
    a[m+1] = c[m+1]/(n+1)
    
pol = a0*np.ones((100, ))
z = np.linspace(A, B, 100)
zm = (z-A)*(r-l)/(B-A)+l

for i in range(1, m+2):
    pol = pol + a[i]*np.cos(i*zm) + b[i]*np.sin(i*zm)
    
    title = "n = " + str(n)
    plt.title(title)
    plt.plot(z, pol, "-r")
    plt.plot(xx, y, 'x')
    plt.show()
    


"""
TrasformataDiFourierES2)
Scrivere uno script che calcoli il polinomio trigonometrico di un opportuno grado
m che interpoli un insieme di punti Pi = (xi; yi), i = 0; :::; n, con xi punti
equidistanti in un intervallo [-3,3] e yi; i = 0; ::n definiti

yi =   { 1 se xi < -1 oppure se xi > i
       { 0 altrimenti;
                                                i = 0; ::; n;

Testare lo script al variare di n e visualizzare il polinomio interpolante parziale
via via che si somma il contributo k-esimo a(k)*cos(kx)+b(k)*sin(kx)
"""

n = 3
A = -2#-math.pi
B = 2#math.pi
step = (B-A)/(n+1)
xx = np.arange(A, B, step)
f = lambda x : np.sinh(x)

#mappo i punti nell'intervallo 0-2pi
l = 0
r = 2*math.pi
xm=(xx-A)*(r-l)/(B-A)+l
 
m = n // 2  #// restituisce l'intero inferiore della divisione
   
y = f(xx)
c = fft(y) #calcola la trasformata di Fourier
a = np.zeros((m+2,)) #array che conterrà la parte reale
b = np.zeros((m+2,)) #array che conterrà la parte immaginaria

a0 = c[0]/(n+1)
a[1:m+1]=2*c[1:m+1].real/(n+1) 
b[1:m+1]=-2*c[1:m+1].imag/(n+1)

if n%2 != 0:
    a[m+1]=c[m+1]/(n+1) 


pol = a0*np.ones((100,))
z = np.linspace(A,B,100)
zm = (z-A)*(r-l)/(B-A)+l

for i in range(1,m+2):
   pol = pol + a[i]*np.cos(i*zm) + b[i]*np.sin(i*zm) 

plt.plot(z,pol,'-r')
plt.plot(xx,y ,'x')
plt.plot(z ,f(z),'-b')
plt.show()


"""
TrasformataDiFourierES3)
Siano (ti,yi) le misurazioni del fusso sanguigno attraverso una sezione dell'arteria
carotide durante un battito cardiaco. La frequenza di acquisizione dei dati
è costante e pari a 10/T dove T = 1 sec. è il periodo del battito.

ti  0    0.1     0.2     0.3     0.4     0.5     0.6     0.7     0.8      0.9
yi  3.7  13.5    5       4.6     4.1     4.5     4       3.8     3.7      3.7

Costruire e visualizzare il polinomio trigonometrico di grado m opportuno che
interpola le coppie di dati e le coppie di dati su uno stesso grafico.
"""

A, B = 0, 1
l, r = 0, 2*math.pi
n = 9
step = (B-A)/(n+1)

x = np.arange(0, 1, 0.1)
y = np.array([3.7, 13.5, 5, 4.6, 4.1, 4.5, 4, 3.8, 3.7, 3.7])

m = n//2

a = np.zeros((m+2, ))
b = np.zeros((m+2, ))
c = fft(y)

a0 = c[0]/(n+1)

a[1:m+1] = 2*c[1:m+1].real/(n+1)
b[1:m+1] = -2*c[1:m+1].imag/(n+1) 

if n%2 != 0:
    a[m+1] = c[m+1]/(n+1)
    
pol = a0 * np.ones((100, ))
z = np.linspace(A, B, 100)
zm = ((z-A)*(r-l)/(B-A) + l)

for i in range(1, m+2):
    pol = pol + a[i]*np.cos(i*zm) + b[i]*np.sin(i*zm)
    
    plt.plot(z, pol, "-r")
    plt.plot(x, y, "x")
    plt.show()


"""
TrasformataDiFourierES4)
Supponiamo di ricevere il segnale sinusoidale f(t) = sin(2pi5t) + sin(2pi10t);
a cui è sovrapposto il rumore dato dalla funzione noise(t) = sin(2pi * 30 * t).
Sia T = 2 la durata in secondi del segnale, e sia campionato ad una frequenza
di 100 campioni al secondo. Dopo aver calcolato i coefficienti di Fourier del
segnale rumoroso, annullare quelli che corrispondono a frequenze maggiori di 10
e ricostruire il segnale filtrato a partire dai coecienti di Fourier filtrati dalla
frequenza spuria. Visualizzare il segnale esatto, il segnale rumoroso, lo spettro
delle frequenze del segnale rumoroso, lo spettro in cui sono state eliminate le
frequenze spurie ed il segnale filtrato.
"""
A, B = 0, 2
l, r = 0, 2*math.pi
n = 200
step = (B-A)/(n+1)

f = lambda x : np.sin(2*np.pi*5*x) + np.sin(2*np.pi*10*x)
noise = lambda x : np.sin(2*np.pi*30*x)

#-----------------------------SEGNALE RUMOROSO---------------------------------
plt.title("Segnale rumoroso")
x = np.linspace(A, B, n)
y = noise(x) + f(x)

plt.plot(x, y, "-r")
plt.show()

c = fftshift(fft(y))


#------------------------SPETTRO SEGNALE RUMOROSO------------------------------
plt.title("Spettro segnale rumoroso")

freq=np.arange(-50,50,0.5)
plt.plot(freq, abs(c))
plt.show()

#------------------------SPETTRO SEGNALE FILTRATO------------------------------
plt.title("Spettro segnale filtrato")

for i in range(len(freq)):
    if abs(freq[i]) > 10:
        c[i] = 0
        
freq=np.arange(-50,50,0.5)
plt.plot(freq, abs(c))
plt.show()

#-----------------------RICOSTRUZIONE SEGNALE FILTRATO-------------------------

yricostruita = ifft(ifftshift(c))

x = np.linspace(A, B, n)
plt.plot(x, f(x), "-b")
plt.plot(x, yricostruita, "-r")
plt.show()