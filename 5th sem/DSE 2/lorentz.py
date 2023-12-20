import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def lorentz(a,t):
    x,y,z=a
    u=np.array([s*(y-x),x*(r-z)-y,x*y-b*z])
    return u
s=10
b=8/3
r=28
x=0.1
y=0.1
z=0.1
x2=0.000001
u0=[x,y,z]
u1=[x2,y,z]
t=np.linspace(0,50,10000)
sol1=odeint(lorentz,u0,t)
sol2=odeint(lorentz,u1,t)
plt.subplot(411)
plt.plot(t,sol1[:,1])
plt.plot(t,sol2[:,1])
plt.subplot(412)
plt.plot(sol1[:,0],sol1[:,2])
plt.subplot(413)
plt.plot(sol1[:,1],sol1[:,0])
plt.subplot(414)
plt.plot(sol2[:,2],sol2[:,0])
plt.show()