import numpy as np
import matplotlib.pyplot as pl
u = [3,2,1,-1]
y = [7,3,2,1]
z = []

def q (teta):
    k=0
    for i in range(len(u)):
        k = k+((y[i]-teta*u[i])**2)
    return k

r = np.linspace(-5,20,100)
w = np.zeros(len(r))
for p in range(len(r)):
    w[p]= q(r[p])

pl.plot(r,w)
pl.show()
