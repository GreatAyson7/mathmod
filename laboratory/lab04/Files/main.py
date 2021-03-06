import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

w = 0.6
g = 0
x0 = 0.4
y0 = 2.1

t0 = 0
tmax = 51
dt = 0.05

t = np.arange(t0,tmax+dt,dt)
v0 = [x0,y0]

def y(v,t):
    x, y = v
    return [y, -1 * np.power(w,2) * x  - g * y]

eq1 = odeint(y,v0,t)
fig1, grph1 = plt.subplots()
grph1.plot(eq1[:,0], eq1[:,1])
fig4, grph4 = plt.subplots()
grph4.plot(t, eq1[:,0])
grph4.plot(t, eq1[:,1])

w = 0.4
g = 0.4

eq2 = odeint(y,v0,t)
fig2, grph2 = plt.subplots()
grph2.plot(eq2[:,0], eq2[:,1])
fig5, grph5 = plt.subplots()
grph5.plot(t, eq2[:,0])
grph5.plot(t, eq2[:,1])

w = 10
g = 0.2

def f(t):
    return 0.5 * cos(2*t)

def y2(v,t):
    x, y = v
    return [y, -1 * np.power(w,2) * x  - g * y - f(t)]

eq3 = odeint(y,v0,t)
fig3, grph3 = plt.subplots()
grph3.plot(eq3[:,0], eq3[:,1])
fig6, grph6 = plt.subplots()
grph6.plot(t, eq3[:,0])
grph6.plot(t, eq3[:,1])
plt.show()
