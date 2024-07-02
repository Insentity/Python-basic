import math
import numpy as np

def f_list(x): return x**3+x*math.exp(x)+1

#List method
v = [2,3,-1]
def f_list(x): return x**3+x*math.exp(x)+1
y = [f_list(x) for x in v]
print(y)



# Array method
v = np.array([2,3,-1])
# def f_array(input): return np.array([x**3+x*math.exp(x)+1 for x in input])    # Convert to array
print(f_list(v))

