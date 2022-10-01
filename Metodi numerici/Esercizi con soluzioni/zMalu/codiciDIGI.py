import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as spl
from scipy.fft  import fft
import sympy as sym
from sympy.utilities.lambdify import lambdify
import math
from scipy.optimize import fsolve
import numpy.linalg as npl#per norma
""""    
    PER FUNZIONE SIMBOLICA
    x = sym.symbols('x')

    fx = np.e**(2*x-2)-sym.cos(x)
    f = lambdify(x, fx, np)
    soluzione = fsolve(f, 1)
    PER DERIVATA PRIMA
    dfx = sym.diff(fx, x, 1)

"""
""""
    DETRMINANTE =>  [a, b]  = ad-bc    npl.det(A)
                    [c, d]    

    MATRICE INVERSA => det(A^-1)    npl.inv(A)
    det(A^-1) = 1/det(A)
    Il determinante dell'inversa di una matrice è uguale al reciproco del
    determinante della matrice di partenza

    
        se A è triangolare: det(A)= prodotto elementi diagonale diagonale
        detA = np.prod(np.diag(U))


    MATRICE TRASPOSTA =>   det(A^T) = det(A)
        scambio le righe con le colonne

    MATRICE ORTOGONALE => ATA = AAT = Id

    MATRICE SIMMETRICA = TRASPOSTA DI SE STESSA
        [ 1, 2,  3 ]
        [ 2, -1, 0 ]
        [ 3, 0,  5 ]
    SEMIDIFINITA POSITIVA

"""
""""
tol=1e-12
"""

def plagr(xnodi, k):
    xzero= np.zeros_like(xnodi)
    n = xnodi.size
    
    if k == 0:
        xzero = xnodi[1:n]
    else:
        xzero = np.append(xnodi[0:k], xnodi[k+1:n])
    num = np.poly(xzero)
    den = np.polyval(num, xnodi[k])
    
    p = num/den
    
    return p

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

def TrapComp(fname,a,b,n):
    h=(b-a)/n
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[1:n])+f[n])*h/2
    return I

    
def SimpComp(fname,a,b,n):
    h=(b-a)/(2*n)
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[2:2*n:2])+4*np.sum(f[1:2*n:2])+f[2*n])*h/3
    return I


def traptoll(fun,a,b,tol):

    Nmax=2048
    err=1
    
    N=1;
    IN=TrapComp(fun,a,b,N);
    
    while N<=Nmax and err>tol :
        N=2*N
        I2N=TrapComp(fun,a,b,N)#trapezi
        err=abs(IN-I2N)/3
        IN=I2N
 
    
    if N>Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        N=0
        IN=[]
 
    return IN,N


def simptoll(fun,a,b,tol):

    Nmax=2048
    err=1
    
    N=1;
    IN=SimpComp(fun,a,b,N);
    
    while N<=Nmax and err>tol :
        N=2*N
        I2N=SimpComp(fun,a,b,N)#simpson
        err=abs(IN-I2N)/15
        IN=I2N
 
    
    if N>Nmax:
        print('Raggiunto nmax di intervalli con traptoll')
        N=0
        IN=[]
 
    return IN,N

def Lsolve(L,b):
    m, n = L.shape
    if n != m:
        print("Non è quadrata errore")
        return [], 1

    if np.all(np.diag(L)) != True:
        print("Non è diagonale")
        return [], 0
    
    x = np.zeros((n,1))

    for i in range(n):
        s = np.dot(L [i, :i], x[:i])
        x[i] = (b[i]-s)/L[i,i]

    return x, 0

def Usolve(U, b):
    m, n = U.shape
    if n != m:
        print("Non è quadrata errore")
        return [], 1

    if np.all(np.diag(U)) != True:
        print("Non è diagonale")
        return [], 0

    x = np.zeros((n,1))

    for i in range(n-1, -1, -1):
        s = np.dot(U[i, i+1 : n], x[i+1: n])
        x[i] = (b[i]- s)/ U[i,i]

    return x, 0

def LUsolve(L, U, P, b):
    Pb = np.dot(P, b)
    y, flag = Lsolve(L, Pb)

    if flag == 0:
        x, flag = Usolve(U, y)
    else:
        return [], flag

    return x, flag

def  LULUsolve(L,U,c):
    #Soluzione del sistema lineare A**2 x= c che equivale a L U L U x =c
    '''   
Conviene utilizzare la strategia proposta , perchè se la matrice A
è mal condizionata, il sistema lineare con matrice A**2 ha un indice di condizionamento dell'ordine del suo
quadrato, quindi conviene risolvere i 4 sistemi lineari con matrici triangolari che hanno indice di
condizionamento sicuramente minore di A**2
'''
    y3,flag=Lsolve(L,c)
    y2,flag=Usolve(U,y3)
    y1,flag=Lsolve(L,y2)
    x,flag=Usolve(U,y1)
    return x

def swapRows(A,k,p):
    A[[k,p],:] = A[[p,k],:]

def LU_pivot(A):

    m,n=A.shape
    flag=0;
    if n!=m:
      print("Matrice non quadrata")
      L,U,P,flag=[],[],[],1 
      return P,L,U,flag
  
    P=np.eye(n);
    U=A.copy();

    for k in range(n-1):     
          p = np.argmax(abs(U[k:n,k])) + k
          if p != k:
              swapRows(P,k,p)
              swapRows(U,k,p)
  #     Eliminazione gaussiana
          U[k+1:n,k]=U[k+1:n,k]/U[k,k]    
          U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n])   
  
    L=np.tril(U,-1)+np.eye(n)   
    U=np.triu(U)      
    return P,L,U,flag

def LU_nopivot(A):
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
          U[k+1:n,k]=U[k+1:n,k]/U[k,k]                                   
          U[k+1:n,k+1:n]=U[k+1:n,k+1:n]-np.outer(U[k+1:n,k],U[k,k+1:n]) 

    L=np.tril(U,-1)+np.eye(n) 
    U=np.triu(U)           
    return P,L,U,flag


#Calcolo l'inversa della matrice B, risolvendo n sistemi lineari aventi come matrice dei coefficienti
#la matrice B e come termine noto le n colonne della matrice identità

#SUCCESSIVAMENTE

#Dal confronto dell'errore relativo commesso dai due metodi, considerando come valore esatto dell'inversa quello calcolato
#facendo uso della funzione inv del pacchetto numpy.linalg, si conclude che il metodo che sfrutta la fattorizzazione LU per
#calcolo dell'inversa e' più accurato rispetto al metodo della serie troncata
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


def iterazione_punto_fisso(gname, x0, nmax, tolx):
    xk = []
    xk.append(x0)
    x1 = gname(x0)
    xk.append(x1)
    it = 1
    d = x1-x0
    
    while it <= nmax and abs(d)>=tolx * abs(x1):
        x0 = x1
        x1 = gname(x0)
        xk.append(x1)
        d = x1-x0
        it = it +1

    if it == nmax:
        print('Numero iterate massime raggiunte')
    
    return x1, it, xk

def stima_ordine(xk,iterazioni):
    p=[]

    for k in range(iterazioni-3):
        num = np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))

        den = np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1]))
        p.append(num / den);
        
    ordine=p[-1]
    return ordine


def sign(x): return math.copysign(1, x)

#Bisezione
def bisez(fname,a,b,tol):
    eps=np.spacing(1)      
                           # np.spacing(1)  restituisce quindi l' eps di macchina.
    fa=fname(a)
    fb=fname(b)
    if sign(fa)==sign(fb):
       print('intervallo non corretto --Metodo non applicabile')
       return [],0,[]
    else:
        maxit=int(math.ceil(math.log((b-a)/tol)/math.log(2)))#numero massimo di iterazioni
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

#Secanti
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
#Di conseguenza l’ordine di convergenza del metodo di Newton modificato è 2.
#da utilizzare quando anche la derivata della radice è zero
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

def metodoQR(x,y,n):
    """
    INPUT
    x vettore colonna con le ascisse dei punti
    y vettore colonna con le ordinate dei punti 
    n grado del polinomio approssimante
    OUTPUT
     a vettore colonna contenente i coefficienti incogniti
 """
 
    H=np.vander(x,n+1)
    Q,R=spl.qr(H)
    y1=np.dot(Q.T,y)
    a,flag=Usolve(R[0:n+1,:],y1[0:n+1])
    return  a