# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 09:01:30 2021

@author: Nicolò
"""

import numpy as np
import matplotlib.pyplot as plt
import ApprossimazioneMinimiQuadrati as QR

x1 = np.array([-3.5,-3, -2, -1.5, -0.5, 0.5, 1.7, 2.5, 3])
y1 = np.array([-3.9, -4.8, -3.3, -2.5, 0.3, 1.8, 4, 6.9, 7.1])

x2 = np.array([-3.14, -2.4, -1.57, -0.7, -0.3, 0, 0.4, 0.7, 1.57])
y2 = np.array([0.02, 1, -0.9, -0.72, -0.2, -0.04, 0.65, 0.67, 1.1])

x3 = np.linspace(0, 3, 12);
y3 = np.exp(x3) * np.cos(4*x3) + np.random.randn(12,)

x4 = [1.001, 1.0012, 1.0013, 1.0014, 1.0015, 1.0016];
y4 = [-1.2, -0.95, -0.9, -1.15, -1.1, -1];

xx = np.linspace(-3.14, 1.57, 100)

#___________________________________________________________________________

A1 = QR.MetodoQR(x1, y1, 3)

p=np.polyval(A1,xx)
plt.plot(xx, p)
plt.plot(x1, y1, 'x')
plt.show()


A2 = QR.MetodoQR(x2, y2, 4)

p=np.polyval(A2,xx)
plt.plot(xx, p)
plt.plot(x2, y2, 'x')
plt.show()

#___________________________________________________________________________

x = np.array([0.0004, 0.2507, 0.5008, 2.0007, 8.0013])
y = np.array([0.0007, 0.0162, 0.0288, 0.0309, 0.0310])
xx = np.linspace(0.0004, 8.0013, 100)

plt.plot(x, y, 'x')

#RETTA
A1 = QR.MetodoQR(x, y, 1)
p = np.polyval(A1, xx)

plt.plot(xx, p)
print("residuo retta: ", str(np.linalg.norm(y-np.polyval(A1, x))**2))

#PARABOLA
A1 = QR.MetodoQR(x, y, 2)
p = np.polyval(A1, xx)

plt.plot(xx, p)
print("residuo parabola: ", str(np.linalg.norm(y-np.polyval(A1, x))**2))

#CUBICA
A1 = QR.MetodoQR(x, y, 3)
p = np.polyval(A1, xx)

plt.plot(xx, p)
print("residuo cubica: ", str(np.linalg.norm(y-np.polyval(A1, x))**2))

plt.show()


















