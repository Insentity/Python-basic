from F2 import F
from math import pi

f = F(a = 1.0, omega = 0.1)

print(f(pi))
f.a = 2
print(f(pi))