import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

a = 0.01
b = 0.02
N = 20000
I = 99
R = 5
S = N - I - R
t = np.arange(0,200,0.01)
v = [S, I, R]

def f1(v,t):
    dS = 0
    dl = -1 * b * v[1]
    dR = b * v[1]
    return [dS, dl, dR]

def f2(v,t):
    dS = -1 * a * v[0]
    dl = a * v[0] - b * v[1]
    dR = b * v[1]
    return [dS, dl, dR]

res = odeint(f1, v, t)
plt.plot(t, res[:,0])
plt.plot(t, res[:,1])
plt.plot(t, res[:,2])
plt.legend(('S(t)', 'l(t)', 'R(t)'))
plt.show()

res = odeint(f2, v, t)
plt.plot(t, res[:,0])
plt.plot(t, res[:,1])
plt.plot(t, res[:,2])
plt.legend(('S(t)', 'l(t)', 'R(t)'))
plt.show()