class Parabola(object):
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2


    def __call__(self, x):
        # print("Parabola")
        return self.c2*x**2 + self.c1*x + self.c0


    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ""
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += "%12g %12g\n" % (x, y)
        return s
    
class sin_plus_quadratic(Parabola):
    def __init__(self, c0, c1, c2, A, w):
        from numpy import pi
        Parabola.__init__(self, c0, c1, c2)
        self.A = A
        self.w = w

    def __call__(self, x):
        from numpy import sin
        print(Parabola.__call__(self, x))
        print(self.A*sin(self.w * x))
        return Parabola.__call__(self, x) + self.A*sin(self.w * x)
    

