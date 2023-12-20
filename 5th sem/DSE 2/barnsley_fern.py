import numpy as np
import matplotlib.pyplot as plt
def func1(x,y):
	return np.array([0.0,0.16*y])
def func2(x,y):
	return np.array([0.85*x+0.04*y , -0.04*x+0.85*y+1.60])
def func3(x,y):
	return np.array([0.20*x-0.26*y , 0.23*x+0.22*y+1.60])
def func4(x,y):
	return np.array([-0.15*x+0.28*y , 0.26*x+0.24*y+0.44])
N=100000
x,y=0.,0.
p=np.random.rand(N)
for i in range(N):
	if p[i]<0.01:
		x,y=func1(x,y)
	elif p[i]<0.86:
		x,y=func2(x,y)
	elif p[i]<0.93:
		x,y=func3(x,y)
	else:
		x,y=func4(x,y)
		plt.plot(x,y, 'o r')
plt.grid(True)
plt.title('Barnsley Fern')
plt.show()