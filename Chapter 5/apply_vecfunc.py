import numpy as np

def f_list(x): return x**3+x*np.exp(x)+1

#List method
v = [2,3,-1]
y = [f_list(x) for x in v]  # Must use for loop
print(y)


# Array method
v = np.array([2,3,-1])      # No for loop needed
print(f_list(v))    

