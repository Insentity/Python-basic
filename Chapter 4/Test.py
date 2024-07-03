from matplotlib.pyplot import *
import numpy as np
from numpy import exp

x = np.linspace(0,3,51)
y = x**2 * exp(-x**2)

lines = plot(x,y)
print(lines)
show()
