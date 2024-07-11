import numpy as np
from matplotlib.pyplot import *

def h(x): return (1/ np.sqrt(2*np.pi)) * np.exp((-1/2)*x**2)

xlist = np.linspace(-4,4,41)
hlist = h(xlist)
plot(xlist, hlist)
show()
