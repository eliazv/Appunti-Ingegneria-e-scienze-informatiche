"""
Funzioni per il calcolo degli zeri di funzioni non lineari
"""
import numpy as np
import math

'''
Il core Python non possiede la funzione sign.
La funzione copysign(a,b)  del modulo math restituisce un valore numerico che ha il valore assoluto di
a e segno di b.
Per avere il segno di un valore numerico b si può usare math.copysign(1,b)
che resistuisce 1 se b>0, -1 se b<0, 0 se b è zero
'''

def sign(x): return math.copysign(1, x)


#Bisezione
def bisez(fname,a,b,tol):
    eps=np.spacing(1)      # np.spacing(x) Restituisce la distanza tra x e il numero adiacente più vicino.
                           # np.spacing(1)  restituisce quindi l' eps di macchina.
    fa=fname(a)
    fb=fname(b)
    if sign(fa)==sign(fb):
       print('intervallo non corretto --Metodo non applicabile')
       return [],0,[]
    else:
        maxit=int(math.ceil(math.log((b-a)/tol)/math.log(2)))
        print('n. di passi necessari=',maxit,'\n');
        xk=[]
        it=0
        #while it<maxit and  abs(b-a)>=tol+eps*max(abs(a),abs(b)):
        while it<maxit and  abs(b-a)>=tol:
            c=a+(b-a)*0.5   #formula stabile per il calcolo del punto medio dell'intervallo
            xk.append(c) 
            it+=1
            if c==a or c==b:
                break
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
#Regula Falsi       
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
                x1=a-fa*(b-a)/(fb-fa);
                xk.append(x1)
                it+=1
                fxk=fname(x1);
                if fxk==0:
                    break
                elif sign(fxk)==sign(fa):
                    a=x1;
                    fa=fxk;
                elif sign(fxk)==sign(fb):
                    b=x1;
                    fb=fxk;
                
                
            if it==nmax :
                print('Regula Falsi: Raggiunto numero max di iterazioni')
                
           
            
        return x1,it,xk
    

def corde(fname,fpname,x0,tolx,tolf,nmax):
 #Corde
        xk=[]
        m=fpname(x0)               #m= Coefficiente angolare della tangente in x0
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
def secanti(fname,xm1,x0,tolx,tolf,nmax):
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
    
def stima_ordine(xk,iterazioni):
      p=[]

      for k in range(iterazioni-3):
         p.append(np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))/np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1])));
     
      ordine=p[-1]
      return ordine

#Newton Modificato
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


     
def iterazione(gname,x0,tolx,nmax):
        
        xk=[]
        xk.append(x0)
        x1=gname(x0)
        d=x1-x0
        xk.append(x1)
        it=1
        while it<nmax and  abs(d)>=tolx*abs(x1) :
            x0=x1
            x1=gname(x0)
            d=x1-x0
            it=it+1
            xk.append(x1)
           
    
        if it==nmax:
            print('Raggiunto numero max di iterazioni \n')
        
        return x1, it,xk