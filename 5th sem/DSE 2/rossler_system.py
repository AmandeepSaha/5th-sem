import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def rossler(d,t):
    x,y,z=d
    u=np.array([-y-z,x+a*y,b+z*(x-c)])
    return u
b=2
c=4
a=0.4
x=0.1
y=0.1
z=0.1
x2=0.001
u1=[x,y,z]
u2=[x2,y,z]
t=np.linspace(0,100,10000)
sol1=odeint(rossler,u1,t)
sol2=odeint(rossler,u2,t)
plt.subplot(411)
plt.plot(t,sol1[:,1])
plt.plot(t,sol2[:,1])
plt.subplot(412)
plt.plot(sol1[:,0],sol1[:,1])
plt.subplot(413)
plt.plot(sol1[:,1],sol1[:,2])
plt.subplot(414)
plt.plot(sol2[:,2],sol2[:,0])
plt.show()