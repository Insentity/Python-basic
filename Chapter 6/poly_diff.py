import numpy as np



p = {0: -3, 3: 2, 5: -1} # -3 + 2*x**3 - x**5

def diff(p):
    result = {}
    for poly in p:
        if poly == 0: continue
        else:
            # print(poly)
            result[poly-1] = p[poly]*poly
    return(result)

result = diff(p)
print(result)  # should be 6*x**2 - 5*x**4: {2: 6, 4: -5}
