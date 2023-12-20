import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

n = 1000
x = np.linspace(10e-4,1,1000)
h = 1973
m = 0.511*10**6
D = 0.755501
alf= 1.44
r0 = 0.131349
E1 = h*2/(2.*m*r0*2)

dx = x[1] - x[0]
def potnetial(x):
    return (D/E1)*(np.exp(-2.*alf*(1.-1./x)) - np.exp(-alf*(1.-1./x)))

T = np.zeros((n-2,n-2))
for i in range(n-2):
    for j in range(n-2):
        if i == j:
            T[i,j] = -2
        elif abs(i-j) == 1:
            T[i,j] = 1
            
V = np.zeros((n-2,n-2))

for i in range(n-2):
    for j in range(n-2):
        if i == j:
            V[i,j] = potnetial(x[i+1])
            
H = (-h**2/(2*m*dx*2))*T + V

vals,vecs = np.linalg.eigh(H)
E = vals[0:4]

psy = np.transpose(vecs)[0:4]
psy = np.insert(psy,[0],np.zeros((4,1)),axis =1)
psy = np.append(psy,np.zeros((4,1)), axis = 1)

print("Energy eigen value: ",E)
for i in range(4):
    plt.plot(x*r0,psy[i])
plt.show()