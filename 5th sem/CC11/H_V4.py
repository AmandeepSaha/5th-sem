# Solving s-wave radial equation of a particle in Morse potential
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

m = 940e6
D = 0.755501
alf= 1.44
r0 = 0.131349
hc = 1973
E1 = hc*2/(2.*m*r0*2)    # Ground state energy


def V(x):       # Effective potential energy function
    return (D/E1)*(np.exp(-2.*alf*(1.-1./x)) - np.exp(-alf*(1.-1./x)))

n = 4000        # Number of intervals
dim = n - 1     # Number of internal points
xl = 0.1        # xl corresponds to origin
xr = 100.       # xr is some large value
h = (xr-xl)/n   # value of each interval

x = np.linspace(xl+h,xr-h,dim)

# print(V(2),V(1000),(D/E1)*(np.exp(-2.*alf) - np.exp(-alf)),h)
# plt.ylim(-2,2)
# plt.plot(x,V(x))

#Fill Hamiltonian

H = np.zeros((dim,dim),float)
for i in range(len(H)-1):
        H[i,i+1] = H[i+1,i] = -1/h**2 

for i in range(len(H)):
        H[i,i] = 2./h**2 + V(x[i]) 

# Calculate eigenvalues and eigenvectors
vals, vecs = linalg.eigh(H)      #Note: eigenvectors are in columns of vecs

# Eigenvalues
print("Ground state energy = {:2.3f} eV".format(vals[0]*E1))
print("1st excitation energy = {:2.3f} eV".format(vals[1]*E1))

# Plot wave functions
plt.title("Morse potential, $\ell = 0$ states")
plt.xlabel("$r$ in $\AA$")
plt.ylabel("$u(r)$")
plt.axhline(0, color='black')     #draw x axis
plt.grid()
plt.xlim(0,1)
plt.plot(x*r0,vecs.T[0], c='b', ls='dashed',
         label="$E_1$ = {:2.3f} eV".format(vals[0]*E1))
plt.plot(x*r0,vecs.T[1], c='r', ls='dashdot',
         label="$E_2$ = {:2.3f} eV".format(vals[1]*E1))
plt.legend()
plt.savefig("Morse.pdf")
plt.show()
