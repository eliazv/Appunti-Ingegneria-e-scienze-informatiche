# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:35:12 2021

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

from funzioni_Sistemi_lineari import LU_nopivot   #importare da altri documenti

tol=1e-12   #di base



"""
---------------------------TEORIA------------------------
"""
"""
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

    DETERMINANTE != 0  ---> matrice ammette la fattorizzazione LU senza pivoting

"""

#FUNZIONI DI BASE
radice1 = np.sqrt(val)        #rad(val)
radice2 = sym.sqrt(val)       #MEGLIO QUESTA
seno = np.sin(val)            #sen(val)
coseno  = np.cos(val)         #cos(val)
allaseconda = x**2            #x^2
pigreco = math.pi             #pi
valoreassoluto = np.abs(val)  #|val|
eallax = np.exp(x)            #e^x   


"""
------------------------FUNZIONI-------------------------
"""

#definizione normale (per derivata)
x = sym.symbols('x')      #definisce simbolo
fx = x - (1/3)*np.sqrt(30*x - 25) #funzione
f = lambdify(x, fx, np)   #valutare la funzione

dfx=sym.diff(fx, x, 1)    #derivata prima(1) di fx su x


#definizione con lambda
f= lambda x: np.tan(3/2*x)-2*np.cos(x)-x*(7-x) 



s1 = sym.Float(a+b,2)     #arrotanda il risultato dell'operazione utilizzando 2 cifre per la mantissa

b = np.array([1.1, 2.33, 1.7])       #crea array

alfa=fsolve(f, x0)                   #calcola la radice

z = spl.solve(array1, array2)        #???

q = 10.0**(-np.arange(0.0,11.0))     # q=10^-i    i=0,...,10


nt=np.zeros((ncampio,));             #indice n della serie ???? £

A=spl.hilbert(4)                     #????  £

residuo=np.linalg.norm(y-np.polyval(a,x))**2 #???? £

p=np.polyval(a,xval)                 #crea polinomio £  (es. np.polyval([3,0,1], 5)  # 3 * 5**2 + 0 * 5**1 + 1  = 76)



#Errore relativo sui dati
err_rel = np.abs(val_esatto - val)/np.abs(val_esatto)  #err_rel=np.abs(exp_app-exp_es)/np.abs(exp_es)

err_dati=npl.norm(A-A1,np.inf)/npl.norm(A,np.inf) #£
print("Errore relativo sui dati  in percentuale ", err_dati*100,"%")






"""
--------------------------INTERVALLO-----------------------
"""
A, B = 5/6, 25/6
xx = np.linspace(A, B, 100)     #crea intervallo tra A e B suddiviso in 100 parti

plt.plot([1, 36], [5, 5])       #linea orizz di valore 5 nell'intervallo 1-35

plt.plot(range(n),u2)           #u2 successione

plt.plot(xx, xx*0, "-k")        #linea orizzontale di valore 0 nell'intervallo xx

xx = np.arange(2, 7, 1)         #da 2 a 6 compreso, passo 1



"""
--------------------------VETTORE--------------------------
"""
y=np.zeros((n,),dtype=float)   #vettore vuoto con n elementi

z=np.array([76.0,92.0,106.0,123.0,132.0,151.0,179.0,203.0,226.0,249.0,281.0,305.0])


"""
---------------------------MATRICE-------------------------
"""
A = np.array([[10, -4, 4, 0], [-4, 10, 0, 2], [4, 0, 10, 2], [0, 2, 2, 0]],dtype=float)

B = np.array([[0.98, 0.02, 0, 0.04, 0],
    [0.08, 0.93, 0.08, -0.07, -0.03],
    [0.04, 0.01, 0.97, -0.07, -0.04],
    [0.02, -0.03, 0, 1.03, 0],
    [0.07, 0.04, 0, -0.08, 1.01]])

C = np.zeros((5,2))  #5 righe, 2 colonne

I=np.eye(n)          #matrice identità    n = num righe

A2 = np.dot(A,A)     #A^2   moltiplicazioni tra matrici

"""
DETERMINANTE
se DETERMINANTE != 0  ---> matrice ammette la fattorizzazione LU senza pivoting
"""
detA=np.prod(np.diag(U))    #DETERMINANTE   U --> calcolata con LU_nopivot(A)
npl.det(A)  #calcola determinante?

detinvA=1/detA      #determinante INVERSA

invA=npl.inv(A)      #calcolo INVERSA?





"""
----------------------------GRAFICO--------------------------
"""
plt.semilogy(range(5,35,5),LLe, range(5,35,5),LLc)   #grafico in scala semilogaritmica (range da 5 a 30 con passo di 5 di 2 funzioni) 
plt.title("f")                #titolo
plt.plot(xx, f(xx), "r--")    #disegna linea (intervallo, funzione, colore e tratteggio)
plt.plot(xx, xx*0, "-k")      #linea orizzontale di valore 0 nell'intervallo xx
plt.legend(['descrizione 1 ', 'descrizione 2']) #legenda
plt.show()


plt.plot(z,f(z),  z,pol,  x,y,'o')      #nel terzo (x,y,'o') appaiono i punti dove di incrociano le funzioni
plt.legend(['Funzione da interpolare','Polinomio interpolatore', 'Nodi di interpolazione'])
plt.show()



"""
-----------------------------STAMPA--------------------------
"""
print("risultato = ", variabile)  



"""
-----------------------------------------ESERCIZI----------------------------------------------------
"""

"""
Implementare successione
"""
c = np.zeros(35)    #vettore di valori nulli
c[0] = 4            #primo valore = 4
c[1] = 17/4         #secondo valore = 17/4 
for i in range(2, 35):                                  #dal terzo in poi
    c[i] = 108 - 815/c[i-1] + 1500/(c[i-1]*c[i-2])      #funzione



"""
Errore relativo
"""
err_rel = abs(val_esatto - val)/abs(val_esatto)
plt.title("errore successione")
plt.semilogy(range(1, 36), err_rel)  #grafico in scala semilogaritmica,  altri modi? plt.plot(range(1, 36), err_rel) £
plt.show()



"""
Converge a 5
"""
plt.title("convergenza successione")
plt.plot(range(1, 36), b)
plt.plot([1, 36], [5, 5])   #linea orizz di val 5 fino al valore 35 sulle x
plt.show()



"""
Valori coincidono
"""
plt.title("succ 1 vs succ 2")
plt.plot(range(1, 36), a, "-b")
plt.plot(range(1, 36), b, "-r")
plt.show()



"""
Calcolare soluzioni         equazioni non lineari?? £
"""
gb = lambda x : 8 - 15/x        #funzione
xkb, itb, flag = metodoIterativoAPuntoFisso(gb, 4, 1e-7, 50)    #(in ZeriDiFunzione)
print(xkb)                      #risultati



"""
Mostrare punto fisso
"""
xx = np.arange(2, 7, 1)     #intervallo
plt.plot(xx, gb(xx), "-r")  #funzione
plt.plot(xx, xx, "-k")      #linea diagonale
plt.show()                  #mostrerà dove si intersecano le due funzioni, quello è il punto fisso



"""
Calcola quanti zeri reali possiede e 
in quali intervalli interi dell'asse reale sono localizzati;
"""
f= lambda x: np.exp(x)-4*x**2   #funzione
xx=np.linspace(-1.0,5.0,100)    #intervallo
plt.plot(xx,0*xx,xx,f(xx))      #linea sullo zero e funzione
plt.show()                      #si cercano gli intervalli dove le due funzioni si intersecano (qui sono [-0.8,0], [0,1] e [4,5])

#calcolo il valore esatto di ciascuno degli zeri della funzione f, prende in input l'iterato iniziale x0
x0=-0.8
alfa0=fsolve(f, x0)
print("Lo zero della funzione e' ",alfa0)
x0=0.5
alfa1=fsolve(f, x0)
print("Lo zero della funzione e' ",alfa1)
x0=4.0
alfa2=fsolve(f, x0)
print("Lo zero della funzione e' ",alfa2)




"""
Radici nell'intervallo [A,B]
"""
#Calcolare
x=sym.symbols('x')
fx= x-1/3*sym.sqrt(30*x-25) #funzione
x0=4
dfx=sym.diff(fx,x,1)    #derivata prima
f=lambdify(x,fx,np)
fp=lambdify(x,dfx,np)   #della derivata
alfa=fsolve(f,x0)           #calcola la radice (import sympy as sym from scipy.optimize import fsolve)
dfxs=fsolve(fp,x0) 
print("La funzione ha uno zero in ", alfa)
print("La derivata di annulla in ", dfxs)   #In x=2 si annula sia la funzione che la sua derivata prima,
                                            #la funzione ha in x=2 uno xero con molteplicita=2 -> *VEDI "convergere ad alpha quadraticamente" *

#Mostrare Grafico
A, B = 5/6, 25/6
xx = np.linspace(A, B, 100)
plt.title("f")
plt.plot(xx, f(xx), "-r")   #funz
plt.plot(xx, xx*0, "-k")    #linea orizz di val zero (senza il *0 sarebbe diagonale)
plt.show()                  #i punti dove si intersecano saranno le radici




"""
Convergere ad alpha quadraticamente
"""
x=sym.symbols('x')
fx= x-1/3*sym.sqrt(30*x-25) #funzione
x0=4
dfx=sym.diff(fx,x,1)    #derivata prima
f=lambdify(x,fx,np)
fp=lambdify(x,dfx,np)   #lambdify della derivata

m=2
tolx=1e-12
tolf=1e-12
nmax=100

#Utilizzo il metodo di Newton Modificato con m=2
x1,it,xk= newton_m(f,fp,x0,m,tolx,tolf,nmax)
print('Zero ',x1,' individuato in ', it,' iterazioni')

#   + metodo iterativo ? TODO £




"""
Ordine di convergenza del metodo
"""
ordine=stima_ordine(xk,it) # in ZeriDiFunzione
print('Ordine di convergenza: ', ordine)




"""
Ben condizionato, Stabile     £ da capire se si intende uno o l'altro
"""
#calcolare fx nell'intervallo, per i valori dove tende a zero è ben condizionato.

p=10**5     #variabile
q=10.0**(-np.arange(0.0,11.0))   #valori su cui verificare quando è stabile/ben condizionato

x = sym.symbols('x')    
fx = -p + np.sqrt(p**2 + q) 

#Si stampano i valori di fx e di q, dove fx diventa 0 sarà ben condizionato.
#In questo caso è stabile per valori di q > 1e-6



"""
Suddividere la finestra grafica in sottofinestre
"""
#2 x 3 sottofinestre
fig=1
Le=np.zeros((200,1));
for n in range(5,35,5):     #grado n = 5 : 5 : 30
    xe=np.linspace(a,b,n+1)
    ye=f(xe)
    pole=InterpL(xe,ye,xx);
    re=np.abs(f(xx)-pole)
    plt.subplots_adjust(hspace=0.5,wspace=0.5)  #per spaziare meglio visivamente i grafici della tabella
    plt.subplot(3,2,fig)                        #2x3 sottofinestre
    plt.plot(xx,np.abs(f(xx)-pole))
    plt.legend(['Equidistanti n='+str(n)])      #legenda
    fig+=1
plt.show()



"""
Metodo iterativo che converge quadraticamente al alfa
"""
#metodo di Newton Modificato con m=2
x1,it,xk= newton_m(f,fp,x0,m,tolx,tolf,nmax)



"""
determinare il polinomio p che interpola f sui nodi 1.0, 1.5, 1.75
"""
f= lambda x: np.cos(math.pi*x)+np.sin(math.pi*x)    #funzione
x=np.array([1.0,1.5,1.75])      #nodi
y=f(x)
xx=np.linspace(0.0,2.0,100)     #punti di valutazione per l'interpolante
pol=InterpL(x,y,xx)             #valori del polinomio



"""
si calcoli il valore assunto dalla funzione resto r(x) := |f(x) - p(x)| nel punto x* = 0:75;
"""
polxs=InterpL(x,y,np.array([0.75]))
err_xs= np.abs(polxs-f(0.75))
print("Funzione resto nel nodo 0.75 uguale a ",err_xs)



"""
Stabilire se la matrice A ammette la fattorizzazione LU senza pivoting
"""
A=np.array([ [10, -4, 4, 0], [-4, 10, 0, 2], [4, 0, 10, 2], [0, 2, 2, 0]],dtype=float)
det_minoreA=[]
for i in range (0,4):
    det_minoreA.append(npl.det(A[:i+1,:i+1]))

if np.all(det_minoreA!=0):
    print("La matrice A ammette fattorizzazione LU no-pivoting")



"""
spiegare perchè la successione (2) converge a 5 mentre la successione (3) converge a 100.
"""
#mostrare che l'unico punto fisso della (4) è 5 mentre l'unico punto fisso della (5) è 100.


#------------------------------------------------------------------------------------------
"""
Supponiamo di ricevere il segnale sinusoidale f(t) = sin(2pi5t) + sin(2pi10t); a cui è sovrapposto il
rumore dato dalla funzione noise(t) = sin(2pi * 30 * t). Sia T = 2 la durata in secondi del segnale, e sia
campionato ad una frequenza di 100 campioni al secondo. Dopo aver calcolato i coefficienti di Fourier
del segnale rumoroso, annullare quelli che corrispondono a frequenze maggiori di 10 e ricostruire il
segnale filtrato a partire dai coefficienti di Fourier filtrati dalla frequenza spuria. Visualizzare il segnale
esatto, il segnale rumoroso, lo spettro delle frequenze del segnale rumoroso, lo spettro in cui sono state
eliminate le frequenze spurie ed il segnale filtrato.
"""
from scipy.fft  import fft, ifft
from scipy.fftpack import fftshift, ifftshift
import math
import numpy as np
import matplotlib.pyplot as plt

#Filtraggio di un segnale nel dominio di FOurier
f= lambda x: np.sin(2*math.pi*5*x)+np.sin(2*math.pi*10*x)
noise= lambda x: 2*np.sin(2*math.pi*30*x)

T=2     #Durata del segnale
Fs=100  # Frequenza di campionamento nel dominio del tempo: Numero di campioni al secondo (maggiore uguale del doppio della freqeunza massima nel dominio delle frequenze
        #(wmax) presente nel segnale)
dt=1/Fs # Passo di campionamento nel dominio del tempo
N=T*Fs  #Numero di campioni: durata in secondi per numero di campioni al secondo

#Campionamento del dominio temporale
t=np.linspace(0,T,N)

#Campionamento del segnale rumoroso
y=f(t)+noise(t)
plt.plot(t,y,'r-')
plt.title('Segnale rumoroso')
plt.show()
plt.plot(t,f(t),'b-')
plt.title('Segnale esatto')
plt.show()

#Passo di campionamento nel dominio di Fourier (si ottiene dividendo per N l'ampiezza del range che contiene le frequenze)
delta_u=Fs/N
freq=np.arange(-Fs/2,Fs/2,delta_u)  #Il range delle frequenza varia tra -fs/2 ed fs/2
c= fftshift(fft(y))

plt.plot(freq,np.abs(c))
plt.title('Spettro Fourier segnale rumoroso')
plt.show()
ind= np.abs(freq)> 10.0     #DATO DA CAMBIARE

#Annulliamo i coefficienti di Fourier esterni all'intervallo di frequenze [-10,10]
c[ind]=0
plt.plot(freq,np.abs(c))
plt.title('Spettro Fourier segnale Filtrato')
plt.show()
#Ricostruiamo il segnale a partire dai coefficienti du Fourier filtrati
rec=ifft(ifftshift(c))
plt.plot(t,rec,t,f(t))
plt.legend(['Segnale filtrato', 'Segnale originale'])


#------------------------------------------------------------------------------------------


"""
si rappresenti in un grafico in scala semilogaritmica sulle y (comando semilogy eventualmente pre-
ceduto da set(gca,'yscale','log')) il vettore dei valori assoluti di tutte le approssimazioni calcolate dal
procedimento iterativo (comprese tra |x(0)| e |alpha|), in funzione del numero di iterazioni compiute;
"""
plt.plot(range(it),np.abs(xk))      # da capire perche non usa semilogy ma plot £
plt.show()


#------------------------------------------------------------------------------------------


"""
si stabilisca se il metodo iterativo proposto al punto b) può convergere ad alpha quadraticamente anche
partendo dall'estremo sinistro dell'intervallo, ossia da x(0) = 1, e si giustifichi la risposta.
"""
#Il metodo non converge se scelgo come iterato iniziale x0=1,
#perchè la derivata prima in 1 diverge  va a -infinito

#DA CAPIRE

#------------------------------------------------------------------------------------------



"""
Si approssima In, n = 1;...; 30 utilizzando la formula dei trapezi composita su N sottointervalli equispaziati,
determinando automaticamente il valore di N affinchè il resto della formula di quadratura composita sia minore di tol = 1.e-6
"""
#Estremi di integrazione (integrale da 0 a 1)
a=0
b=1
I=[]

for n in range(1,31):
    f= lambda x: x**n/(x+10)
    tol=1e-6
    I1t,N1=traptoll(f,a,b,tol)
    I.append(I1t)

plt.plot(I,'r-o')
plt.show()


#------------------------------------------------------------------------------------------



"""
si approssima In, n = 1; : : : ; 30 con il valore yn, n = 1; : : : ; 30 ottenuto dall'algoritmo ricorsivo 
      y1 = log(11)-log(10)   yn+1 = 1/n - 10yn;   n = 1;...; 29
"""
y=np.zeros((n,),dtype=float)    # n? £
y[0]=np.log(11)-np.log(10)      # primo valore y1 = log(11)-log(10)
for n in range(1,30):           # n = 1;...; 29
    y[n]=1/n-10*y[n-1]          # yn+1 = 1/n - 10yn


    
"""
Se fosse da n = 30,...,1
"""
for n in range(31,0,-1):
    z[n-1]=1/10*(1/n-z[n])




#------------------------------------------------------------------------------------------



"""
Si rappresenti in un grafico in scala semilogaritmica sulle y (comando semilogy)
- l'andamento dell'errore relativo tra yn e In,
- l'andamento dell'errore relativo tra zn e In,
al variare di n = 1,..., 30, assumendo come valore esatto per In quello calcolato al punto a);
"""
err_rel_y=np.abs(y-I)/np.abs(I)
err_rel_z=np.abs(z[0:nval]-I)/np.abs(I)
plt.semilogy(np.arange(nval),err_rel_y,'g-.',np.arange(nval),err_rel_z,'b--')
plt.legend(['Errore relativo algoritmo b ', 'Errore relativo algoritmo c'])

#il più stabile è quello con i valori più bassi



#------------------------------------------------------------------------------------------



"""
Si utilizzi la function Matlab metodoQR per determinare i polinomi di approssimazione ai minimi quadrati 
di grado 1, 2 e 3 dei dati assegnati in tabella, e si rappresentino in uno stesso grafico i dati
(xi; yi), i = 1;...; 12 e i tre polinomi determinati.
"""
m=12
x=np.linspace(1900,2010,12) #1900, 1910, 1920, ... , 2010.
y=np.array([76.0,92.0,106.0,123.0,132.0,151.0,179.0,203.0,226.0,249.0,281.0,305.0])
#intervallo
xmin=np.min(x)
xmax=np.max(x)
xval=np.linspace(xmin,xmax,100)

for n in range(1,4):
    a=metodoQR(x,y,n)       #n grado

    residuo=np.linalg.norm(y-np.polyval(a,x))**2        #Da capire £
    print("Norma del residuo al quadrato",residuo)      
    
    p=np.polyval(a,xval)                                #crea polinomio 
    plt.plot(xval,p)        #disegna polinomio
    
plt.legend(['n=1','n=2','n=3']) 
plt.plot(x,y,'o')

#Quale tra le tre approssimazioni ottenute al punto precedente risulta migliore? Confrontare gli errori
#dove f1, f2 e f3 denotano i polinomi di approssimazione di grado 1, 2 e 3 determinati al punto c).         #da capire £




#------------------------------------------------------------------------------------------




"""
si costruiscano, per i = 0;...; 5, le ordinate yi= { 2/pi integrale da 0 a xi( 5.5(1-e^-0.05t)sen(t^2)) dt } 
utilizzando la formula di Simpson composita su Ni sottointervalli equispaziati in cui il valore di Ni
è determinato automaticamente affinche il resto della formula di quadratura composita sia minore di tol = 1.e -8;
"""
#funzioni per l'integrazione Simposon Composita e con ricerca automatica del numero di N #di sottointervalli
def SimpComp(fname,a,b,n):
    h=(b-a)/(2*n)
    nodi=np.arange(a,b+h,h)
    f=fname(nodi)
    I=(f[0]+2*np.sum(f[2:2*n:2])+4*np.sum(f[1:2*n:2])+f[2*n])*h/3
    return I        

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

tol=1e-08
x=np.zeros((6,))    #per i = 0;...; 5
y=np.zeros((6,))
N=np.zeros((6,))
fig=1
f= lambda x: 2/math.pi*(5.5*(1-np.exp(-0.05*x))*np.sin(x**2)) #Funzione integranda

for i in range(0,6):    #per i = 0;...; 5
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



"""
si dica quanti sottointervalli Ni sono stati necessari per il calcolo di ciascun yi, i = 0;...; 5;
"""
print("Numero di sottointervalli per ciascuni il calcolo di ciascun integrale \n",N)


"""
si costruisca il polinomio di interpolazione di Lagrange dei dati (xi; yi), i = 0;...; 5;
"""
def plagr(xnodi,k):
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

def InterpL(x, f, xx):
     n=x.size
     m=xx.size
     L=np.zeros((n,m))
     for k in range(n):
        p=plagr(x,k)
        L[k,:]=np.polyval(p,xx)

     return np.dot(f,L)
 

pol=InterpL(x, y, xx) #x, y vettori; xx intervallo




"""
si rappresentino in uno stesso grafico i punti di interpolazione (xi; yi), i = 0;...; 5 e il polinomio di
interpolazione ottenuto al punto precedente
"""
plt.plot(xx,pol,  x,y,'ro')
plt.legend(['Polinomio interpolante','Nodi di interpolazione'])
plt.show()


#------------------------------------------------------------------------------------------


"""
Si dica se la matrice B assegnata ammette fattorizzazione LU senza pivoting;
"""
#Verifico che la matrice B abbia i minori principali a rango massimo, ed in caso affermativo posso utilizzare
# il metodo di fattorizzazione di Gauss senza pivoting parziale a perno massimo
det_minoreB=[]
for i in range (0,n):
    det_minoreB.append(npl.det(B[:i+1,:i+1]))
    
if np.all(det_minoreB!=0):
    print("La matrice B ammette fattorizzazione LU no-pivoting")
    



P,L,U,flag=LU_nopivot(B)

#------------------------------------------------------------------------------------------

"""
Si stimi il numero N di sottointervalli equispaziati che servono per approssimare con
la formula di Simpson composita i due integrali (il cui valore esatto è rispettivamente
I1 = 2:114381916835873 e I2 = 2:168048769926493) nel rispetto della tolleranza 10^-5.
Quanto vale N nei due casi? Quanto valgono |~I1 - I1| e |~I2 - I2|?
"""

#Stima del numero N si sottointervalli per approssimare l'integrale della funzione integranda con precisione tol
tol=1e-5
I1t,N1=simptoll(f,a,b,tol)

#Stima del numero N si sottointervalli per approssimare l'integrale del polinomio interpolatore di grado 3 con precisione tol
I2t,N2=simptoll(fpol,a,b,tol)


#I1 ed I2 sono i valori esatti dei due integrali 
I1 = 2.114381916835873
I2 = 2.168048769926493

err1=abs(I1t-I1)
err2=abs(I2t-I2)

print('Errore integrale funzione f(x)', err1,' Numero di suddivisioni ', N1)
print('Errore integrale del polinomio interpolatore', err2, 'Numero di suddivisioni ',N2)



#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------




#da controllare
"""
Nodi di chebyshev
"""
def zeri_Cheb(a,b,n):
    t1=(a+b)/2
    t2=(b-a)/2
    x=np.zeros((n+1,))
    for k in range(n+1):
        x[k]=t1+t2*np.cos(((2*k+1)/(2*(n+1))*math.pi))  #funzione data

    return x

def zeri_Cheb(n):
    x=np.zeros((n+1,))
    for k in range(n+1):
        x[k]=np.cos(((2*k+1)/(2*(n+1))*math.pi))

    return x