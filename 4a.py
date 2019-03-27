import numpy as np
import matplotlib.pyplot as pl
import random as rn

u = [-2, 0, 2, 1, -1]
y = [4, 6, 8, 7, 5]
y1 = []
gora, dol = 0, 0
for i1 in range(len(u)):
    gora = (y[i1]**2) - (u[i1]*y[i1]) + gora
    dol = y[i1] + dol
tet = gora / dol
print(tet)
for i2 in range(len(u)):
    y1.append(tet*u[i2])

print(u, y, y1)
pl.scatter(u, y)
pl.scatter(u, y1, s=50, c='black')
pl.plot(u, y1, 'r')

pl.show()
