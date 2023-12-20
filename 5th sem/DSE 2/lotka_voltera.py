import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def func(u,t):
	x,y=u
	du=np.array([a*x-b*x*y,c*x*y-d*y])
	return du
a=1.1
b=0.4
c=0.1
d=0.4
t=np.linspace(0,100,10000)
for i in range(5):
		y0=[0.1*i,0.2*i]
		sol=odeint(func,y0,t)
		plt.subplot(212)
		plt.plot(sol[:,0],sol[:,1])
plt.subplot(211)
plt.plot(t,sol[:,0])
plt.plot(t,sol[:,1])
plt.grid(True)
plt.title('Lotka voltera Equation')
plt.show( )