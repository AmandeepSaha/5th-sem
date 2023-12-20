import numpy as np
import matplotlib.pyplot as plt
def func(x,r):
	return r*x*(1-x)
n=1000
I=1000
k=998
r=np.linspace(0,6,n)
x=0.5*np.ones(n)
for i in range(I):
	x=func(x,r)
	if i>(I-k):
		plt.plot(r,x,',b')
plt.grid(True)
plt.title('Logistic Map')
plt.show()