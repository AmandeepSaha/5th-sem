import numpy as np 
import matplotlib.pyplot as plt
def funcV(x):
    return((-e**2)/x)
e=3.795
h=1973
m=0.511*10**6
n=100
x=np.linspace(1e-4,10,100)
dx=x[1]-x[0]
T=np.zeros((n-2,n-2))
for i in range(n-2):
    for j in range(n-2):
        if i==j:
            T[i,j]=-2
        elif abs(i-j)==1:
            T[i,j]=1
V=np.zeros((n-2,n-2))
for i in range(n-2):
    for j in range(n-2):
        if i==j:
            V[i,j]=funcV(x[i+1])

H=(-h**2/(2*m*dx*2))*T + V
vals,vecs=np.linalg.eigh(H)
E=vals[0:4]
psi=np.transpose(vecs)[0:4]
psi=np.insert(psi,[0],np.zeros((4,1)),axis=1)
psi=np.append(psi,np.zeros((4,1)),axis=1)
print(E)
for i in range(4):
    plt.plot(x,(psi[i,:])**2,label= +E[i])
plt.grid(True)
plt.xlabel('x')
plt.ylabel('probability density')
plt.title("plot of x vs probability density")
plt.legend(loc="best")
plt.show()

for i in range(4):
    w=np.argmax((psi[i,:])**2)
    xnew=x[w]
    print(xnew)