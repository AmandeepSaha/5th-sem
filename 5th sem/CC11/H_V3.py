# Solving s-wave radial equation of a particle in anisotropic LHO potential
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

m = 940.
k = 100.
b = 30.
hc= 197.3
omega = np.sqrt(k/m) # frequency
a = np.sqrt(hc/(m*omega)) # unit of length

def V(x):       # Effective potential energy function
    return x*2 + (2./3.)*(b/k)*a*x*3

n = 4000        # Number of intervals
dim = n - 1     # Number of internal points
xl = 0.         # xl corresponds to origin
xr = 20.        # xr is some large value
h = (xr-xl)/n   # value of each interval

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
E0 = hc*omega/2.    # Zero point energy
print("Ground state energy = {:2.3f} MeV".format(vals[0]*E0))
print("1st excitation energy = {:2.3f} MeV".format(vals[1]*E0))

# Plot wave functions
plt.title("3D anisotropic Linear Harmonic Oscillator, $\ell = 0$ states")
plt.xlabel("$r$ in fm")
plt.ylabel("$u(r)$")
plt.axhline(0, color='black')     #draw x axis
plt.grid()
plt.xlim(0,5)
plt.plot(x*a,vecs.T[0], c='b', ls='dashed',
         label="$E_0$ = {:2.3f} MeV".format(vals[0]*E0))
plt.plot(x*a,vecs.T[1], c='r', ls='dashdot',
         label="$E_1$ = {:2.3f} MeV".format(vals[1]*E0))
plt.legend()
plt.savefig("aniso3DLHO.pdf")
plt.show()



