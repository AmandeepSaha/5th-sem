# Python code to solve radial part of Hydrogen atom problem
# To fing ground state energy
# Department of Physics
# Sukanta Mahavidyalaya
#--------------------------------------------------------------
import numpy as np
from scipy.integrate import odeint, simps
from scipy.optimize import newton, bisect
from matplotlib import pyplot as plt
from scipy import optimize
#---------------------------------------------------------------
# Derivative function for Schrondiger's equation
def f(w,r,l,En):
    "Given y=[u,u'] returns dy/dr=[u',u''] "
    u, v = w
    f1, f2 = v, (l*(l+1)/r**2-2/r-En)*u
    return [f1, f2]
#-----------------------------------------------------    
r = np.linspace(1e-20,20,500)   # To avoid singularity
l=0
n=1
En=-1/n**2.
w= [0.0, -0.001]                # Boundary condition for shooting Method
rr=r[::-1]                      # We start from large distance
#-------------------------------------------------------
# To calculate probability of finding the electron

while (n<=3):
    En=-1/n**2
    sol = odeint(f, w, rr, args=(l,En))
    psi = sol[:,0][::-1]           # we take psi(r) and invert it in r.
    norm=simps(psi**2,r)
    psi *= 1./np.sqrt(norm)
    plt.plot(r,psi*psi)
    n += 1
plt.grid()
plt.xlabel('r in terms of Borh radius ($a_0=1$)')
plt.ylabel('$|\psi|^2$')
plt.show()
#------------------------------------------------------------

# Shooting Function
def Shoot(En,r,l):              
    rr=r[::-1]
    sol=odeint(f, w, rr, args=(l,En))  # Integrate the Schroedinger equation down to  r=0 .
    psi=sol[:,0][::-1]
    norm=simps(psi**2,x=r)
    psi *= 1./np.sqrt(norm)
    return psi[0]                 #If the energy of the state corresponds to the bound state,
 
#--------------------------------------------------------------

# Energy search from the energy domain
def E_Search(r,l,n_max,Energy):
    n=0
    E=[]
    u0 = Shoot(Energy[0],r,l)
    for i in range(1,len(Energy)):
        u1 = Shoot(Energy[i],r,l)
        if u0*u1<0:
            En = optimize.brentq(Shoot,Energy[i-1],Energy[i],xtol=1e-16,args=(r,l))
            E.append((l,En))
            if len(E)>n_max: break
            n+= 1
            E_theory= -1.0/(n+l)**2
            print ('Computed E=%10.5f |||| E_theory=%10.5f for (n=%d,l=%d)' % (En, E_theory,n,l))
        u0=u1
    
    return E
#------------------------------------------------------------------------
#To calculate the Bound state energy
r = np.logspace(-6,2.2,500)           # Distance in log scale
Energy = -1.2/np.arange(1,20,0.2)**2  # Domain of energy scale
n_max=3
Bnd=[]
for l in range(n_max-1):
    E = E_Search(r,l,n_max-l,Energy)
#-----------------------------------------------------------
#EOF







