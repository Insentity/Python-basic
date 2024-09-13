import Central
import sympy
from math import sin


def f(x):
    return 0.25*x**4 + 10*x

diff = Central.Central(f, h=10E-4)
x = 2
print ("df(%g)=%g" % (x, diff(x)))
print ("exact:", x**3 + 10)


# Sympy function part c/
f_expr = "x*sin(2*x)"
x = sympy.Symbol('x')
f = sympy.lambdify([sympy.Symbol('x')],f_expr)

x_list = (0,1,2,3,4,5,6)
diff = Central.Central(f)
print(diff(x=5))

Central.table(f_expr, x_list)