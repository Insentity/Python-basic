from typing import Any


class F(object):

    def __init__(self, a, omega):
        self.a = a
        self.omega = omega

    def value(self, x):
        from math import exp, sin
        return (exp(-self.a * x) * sin(self.omega*x))
    
    # Call special method 
    def __call__(self, x):
        from math import exp, sin
        return (exp(-self.a * x) * sin(self.omega*x))
    
    # String special method
    def __str__(self):
        return("exp(-a*x) * sin(w*x)")
    

