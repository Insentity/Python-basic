import numpy as np
from matplotlib.pyplot import *


v0 = float(input("Enter v0:"))
g = 9.81
t = np.linspace(0,2*v0/g)

def y(t): return v0*t -0.5*g*t**2
res = y(t)

plot(t, res)
xlabel("time (s)")
ylabel("height (m)")
axis([min(t), max(t), min(res), max(res)+3]) # [tmin, tmax, ymin, ymax]
show()

