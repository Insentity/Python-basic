class F(object):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, t):
        from numpy import exp, sin
        return exp(-self.a*t)*sin(self.b*t)
    
class Fb(F):
    def __init__(self, t, a):
        F.__init__(self, a, b=0)
        self.t = t
        
    def __call__(self, b):
        self.b = b
        return F.__call__(self, self.t)
        