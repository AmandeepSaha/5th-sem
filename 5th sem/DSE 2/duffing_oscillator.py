import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def duffing(u,t):
    du=np.array([u[1],g*np.cos(w*t)-d*u[1]-a*u[0]-b*u[0]**3])
    return du
d=0.3
a=-1
b=1
w=1.2
g=0.5
u1=[0.1,0.2]
u2=[0.1,0.002]
t=np.linspace(0,100,100000)
sol1=odeint(duffing,u1,t)
sol2=odeint(duffing,u2,t)
plt.subplot(311)
plt.plot(t,sol1[:,0])
plt.plot(t,sol2[:,0])
plt.subplot(312)
plt.plot(sol1[:,0],sol1[:,1])
plt.subplot(313)
plt.plot(sol2[:,0],sol2[:,1])
plt.show()