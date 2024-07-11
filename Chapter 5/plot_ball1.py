import numpy as np
from matplotlib.pyplot import *


v0 = 10
g = 9.81
t = np.linspace(0,2*v0/g)

def y(t): return v0*t -0.5*g*t**2
plot(t, y(t))
xlabel("time (s)")
ylabel("height (m)")
show()

