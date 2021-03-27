import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N = 800
n = 11

a_1 = 0.21
a_2 = 0.00008
t = np.arange(0,5,0.1)
dn_max = [-1,-1]

def f(n,t):
    dn = (a_1 + a_2*n)*(N-n)
    return dn
res = odeint(f,n,t)

res = odeint(f,n,t)
plt.plot(t,res[:,0])
plt.show()

a_1 = 0.000012
a_2 = 0.8
t = np.arange(0,0.02,0.00001)

def f(n,t):
    dn = (a_1+a_2*n)*(N-n)
    global dn_max
    if dn > dn_max[0]:
        dn_max = [dn,t]
    return dn

res = odeint(f,n,t)
print(dn_max[1])
plt.plot(t,res[:,0])
plt.show()

a_1 = 0.1
a_2 = 0.1
t = np.arange(0,0.5,0.01)

def f2(n,t):
    dn = (a_1*np.sin(t)+a_2*np.cos(10*t)*n)*(N-n)
    return dn

res = odeint(f2,n,t)
plt.plot(t,res[:,0])
plt.show()
