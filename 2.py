import numpy as np
import matplotlib.pyplot as pl
import random as rn

u = [2,1,-1]
y = [3,2,1]

def q (teta):
    k=0
    for i in range(len(u)):
        k = k+((y[i]-teta*u[i])**2)
    return k
dl =100
r = np.linspace(-20,20,dl)
w = np.zeros(len(r))
for p in range(len(r)):
    w[p]= q(r[p])

minima = []
indexy =[]
m = int(rn.randint(0,dl-1))
mini = w[m]
indexy.append(r[m])
minima.append(mini)
print(m)
s=0

while s<100 :
    m = int(rn.randint(0,dl-1))
    x = w[m]
    print(m)
    if x < mini:
        mini = x
        s=0
        indexy.append(r[m])
        minima.append(mini)
    else:
        s= s+1


pl.plot(r,w,'r')
pl.scatter(indexy,minima)
pl.show()
