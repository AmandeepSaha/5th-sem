# Solving s-wave radial equation of a Hydrogen atom
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

a0 = 0.529177249 # Bohr radiaus

def V(x):    # Effective potential energy function
    return - 2/x

n = 4000        # Number of intervals
dim = n - 1     # Number of internal points
xl = 0          # xl corresponds to origin
xr = 40.        # xr is some large value
h = (xr-xl)/n   # value of each interval
        
h = (xr-xl)/n
x = np.linspace(xl+h,xr-h,dim)

#Fill Hamiltonian

H = np.zeros((dim,dim),float)
for i in range(len(H)-1):
        H[i,i+1] = H[i+1,i] = -1/h**2 

for i in range(len(H)):
        H[i,i] = 2./h**2 + V(x[i]) 

# Calculate eigenvalues and eigenvectors
vals, vecs = linalg.eigh(H)      #Note: eigenvectors are in columns of vecs

# Eigenvalues
E1 = 13.6    # Ground state energy of Hydrogen atom in eV
print("Ground state energy = {:2.3f} eV".format(vals[0]*E1))
print("1st excitation energy = {:2.3f} eV".format(vals[1]*E1))

# Plot wave functions
plt.title("Hydrogen Atom, $\ell = 0$ states")
plt.xlabel("$r$ in $\AA$")
plt.ylabel("$u(r)$")
plt.axhline(0, color='black')     #draw x axis
plt.grid()
plt.xlim(0,10)
plt.plot(x*a0,vecs.T[0], c='b', ls='dashed',label="$E_1$ = {:2.3f} eV".format(vals[0]*E1))
plt.plot(x*a0,vecs.T[1], c='r', ls='dashdot',label="$E_2$ = {:2.3f} eV".format(vals[1]*E1))
plt.legend()
plt.savefig("Hydrogen.pdf")
plt.show()
