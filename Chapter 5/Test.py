import numpy as np


r = np.zeros(100000000)
x = np.random.randint(0, 20, size =100000000)
@profile
def axpy1(r,x):
    r = r + x
    return r
axpy1(r,x)

@profile
def axpy2(r,x):
    r += x
    return r
axpy2(r,x)
