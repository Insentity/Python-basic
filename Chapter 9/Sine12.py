class FuncWithDerivatives(object):
    def __init__(self, h=1.0E-5):
        self.h = h # spacing for numerical derivatives

    def __call__(self, x):
        raise NotImplementedError\
        ("___call__ missing in class %s" % self.__class__.__name__)

    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)

    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        #Compute second derivative by a finite difference:
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)
    

class Sine1(FuncWithDerivatives):
    def __init__(self, h=0.00001):
        FuncWithDerivatives.__init__(self)

    def __call__(self, x):
        from numpy import sin
        return sin(x)
    
class Sine2(FuncWithDerivatives):
    def __init__(self, h=0.00001):
        FuncWithDerivatives.__init__(self)

    def __call__(self, x):
        from numpy import sin
        return sin(x)
    
    def df(self, x):
        from numpy import cos
        return cos(x)
    
    def ddf(self, x):
        from numpy import sin
        return sin(x)
    

    
"""
class MyFunc(FuncWithDerivatives):
    def __init__(self, a):
    self.a = a

    def __call__(self, x):
        return cos(self.a*x) + x**3

    def df(self, x):
        a = self.a
        return -a*sin(a*x) + 3*x**2

    def ddf(self, x):
        a = self.a
        return -a*a*cos(a*x) + 6*x
"""

# Test
""" 
from Sine12 import *

a = Sine1()
b = Sine2()

print("%g %g %g" %(a(5), a.df(5), a.ddf(5)))
print("%g %g %g" %(b(5), b.df(5), b.ddf(5)))
"""