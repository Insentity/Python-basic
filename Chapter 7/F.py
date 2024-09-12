class F(object):

    def __init__(self, a, omega):
        self.a = a
        self.omega = omega

    def value(self, x):
        from math import exp, sin
        return (exp(-self.a * x) * sin(self.omega*x))
    

