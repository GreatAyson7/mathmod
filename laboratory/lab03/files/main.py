import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

x0 = 20500
y0 = 21500
t0 = 0
a = 0.21
b = 0.74
c = 0.68
h = 0.19

tmax = 1
dt = 0.05

t = np.arange(t0, tmax+dt, dt)

def P1(t):
    return np.sin(t)+0.5

def Q1(t):
    return np.cos(t)+0.5

def f1(v, t):
    x, y=v
    return [-a * x - b * y +P1(t), -c * x - h * y +Q1(t)]

v0 = [x0,y0]
eq1 = odeint(f1, v0, t)

fig1, grph1 = plt.subplots()
grph1.plot(t, eq1[:, 0], label='Армия X')
grph1.plot(t, eq1[:, 1], label='Армия Y')
grph1.set_xlabel('Время')
grph1.set_ylabel('Численность армии')
grph1.set_title("Модель боеввых действий №1")
grph1.legend()

plt.show()

a = 0.09
b = 0.79
c = 0.62
h = 0.11

def P2(t):
    return np.sin(2*t)

def Q2(t):
    return np.cos(2*t)

def f2(v, t):
    x, y=v
    return [-a * x - b * y +P2(t), -c * x * y - h * y +Q2(t)]

eq2 = odeint(f2, v0, t)

fig2, grph2 = plt.subplots()
grph2.plot(t, eq2[:, 0], label='Армия X')
grph2.plot(t, eq2[:, 1], label='Армия Y')
grph2.set_xlabel('Время')
grph2.set_ylabel('Численность армии')
grph2.set_title("Модель боеввых действий №2")
grph2.legend()

plt.show()


