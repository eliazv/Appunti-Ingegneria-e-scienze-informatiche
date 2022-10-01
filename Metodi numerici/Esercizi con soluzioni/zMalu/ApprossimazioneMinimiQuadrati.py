# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 08:47:06 2021

@author: Nicolò
"""

import numpy as np
import scipy.linalg as spl
from FattorizzazioneLU import U_solve

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