# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:54:05 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
import InterpolazioneLagrange as lag

f = lambda x : np.cos(np.pi * x) + np.sin(np.pi * x)
xx = np.linspace(0, 2, 100)
nodi = np.array([0.75, 1, 1.5, 1.75])
plag = lag.InterpL(nodi, f(nodi), xx)

plt.plot(xx, f(xx))
plt.plot(xx, plag)
for i in nodi:
    plt.plot(i, f(i), 'o')
plt.show()

err = abs(f(xx) - plag)/abs(f(xx))

plt.semilogy(xx, err)