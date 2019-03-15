import numpy as np
import matplotlib.pyplot as pl


u = [2,1,-1]
y = [3,2,1]

def q (teta):
    k=0
    for i in range(len(u)):
        k = k+((y[i]-teta*u[i])**2)
    return k
a=0
b=2001
dl = b-a
r = np.linspace(-71,27,dl)
w = np.zeros(len(r))
for p in range(len(r)):
    w[p]= q(r[p])
    
pol = int(dl/2)
polowy=[]
pola=[]

while dl>1 :
    pol= int(dl/2)+a
    p1=w[pol-1]
    p2=w[pol+1]
    if p1 < p2:
        b = int(pol)
    else:
        a = int(pol)
    dl = b-a
    print(dl)
    polowy.append(w[pol])
    pola.append(r[pol])
    
    
pl.plot(r,w,'r')
pl.scatter(pola,polowy)
pl.show()
