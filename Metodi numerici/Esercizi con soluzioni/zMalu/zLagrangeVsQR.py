# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:37:58 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
import ApprossimazioneMinimiQuadrati as QR
import InterpolazioneLagrange as Lag

f = lambda x : np.cos(np.pi * x) + np.sin(np.pi * x)
xx = np.linspace(0, 2, 100)
xnodi = np.array([0.25, 1, 1.5, 1.75])

#polinomio di lagrange
plagr = Lag.InterpLag(xnodi, f(xnodi), xx)

#minimi quadrati
A = QR.MetodoQR(xnodi, f(xnodi), 3)
pQR = np.polyval(A, xx)

plt.plot(xnodi, f(xnodi), "o")
plt.plot(xx, f(xx), "-k")
plt.plot(xx, plagr, "-b")

plt.show()

plt.plot(xnodi, f(xnodi), "o")
plt.plot(xx, f(xx), "-k")
plt.plot(xx, pQR, "-b")