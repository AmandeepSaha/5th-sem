import numpy as np
import matplotlib.pyplot as plt
def func(x,y,a,b):
	return np.array([y,-b*x+a*y-y**3])
n=1000
I=1000
k=200
b=0.2
a=np.linspace(0,2.77,n)
x=0.5*np.ones(n)
y=0.5*np.ones(n)
for i in range(I):
	x,y=func(x,y,a,b)
	if i>(I-k):
		plt.plot(a,x,',g')
plt.grid(True)
plt.title('Duffing Map')
plt.show( )