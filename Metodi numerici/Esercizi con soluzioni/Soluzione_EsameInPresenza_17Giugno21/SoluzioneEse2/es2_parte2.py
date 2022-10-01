# -*- coding: utf-8 -*-
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

"""
Filtraggio di un segnale nel dominio di FOurier
"""
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
ind= np.abs(freq)> 10.0

#Annulliamo i coefficienti di Fourier esterni all'intervallo di frequenze [-10,10]
c[ind]=0
plt.plot(freq,np.abs(c))
plt.title('Spettro Fourier segnale Filtrato')
plt.show()
#Ricostruiamo il segnale a partire dai coefficienti du Fourier filtrati
rec=ifft(ifftshift(c))
plt.plot(t,rec,t,f(t))
plt.legend(['Segnale filtrato', 'Segnale originale'])



