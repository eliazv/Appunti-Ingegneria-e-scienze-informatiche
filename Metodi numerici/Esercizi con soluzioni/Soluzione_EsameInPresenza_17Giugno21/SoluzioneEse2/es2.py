# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:55:06 2021

@author: damia
"""
#Per la giustificazione teorica dei risultati guardare il file pdf allegato

import numpy as np
p=10.0**5
q=10.0**(-np.arange(0.0,11.0))


#PUNTO A : si stabilisca se il problema relativo al calcolo della soluzione x = -p + radice(p^2 + q) risulta essere ben condizionato per tutti i valori di q assegnati;
#PUNTO B : si calcoli la soluzione x dell'equazione quadratica (??) mediante la formula risolutiva indicata al punto a) e si dica se l'algoritmo di calcolo risulta numericamente stabile per i valori di q assegnati;

#Valutazione della soluzione con l'algoritmo 1
x1=-p+np.sqrt(p**2+q)
print("x1 =",x1)
print("L'algoritmo 1. è stabile per valori di q > 1e-6 ")  #perche??????

#Affinchè il problema sia ben condizionato, bisogna escludere i valori di q per cui f(q) tende a zero



#PUNTO C : si calcoli la soluzione x dell'equazione quadratica (??) p mediante la formula risolutiva x = q/(p + rad(p^2 + q)) e si dica se l'algoritmo di calcolo risulta numericamente stabile per i valori di q assegnati

#Valutazione della seconda funzione
x2= q/(p+np.sqrt(p**2+q))
print("x2 =",x2)
print("L'algoritmo 2. è stabile per tutti i valori di q assegnati") #perche?????