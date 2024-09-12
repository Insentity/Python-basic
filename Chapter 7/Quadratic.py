class Quadratic(object):
    def __init__(self, a,b,c):
        self.a, self.b, self.c = float(a), float(b), float(c)

    def value(self, x):
        a,b,c = self.a, self.b, self.c
        return(a*x**2 + b*x + c)
    
    def table(self, interval = [0,1], n=1):
        import numpy as np
        x = np.linspace(interval[0], interval[1], num = n)
        print("%-15s" %"x" + "f(x)")
        for item in x:
            print("%-15s" %item + "%-15s" %self.value(item))

    def roots(self):
        from math import sqrt
        a,b,c = self.a, self.b, self.c
        D = b**2 - 4*a*c

        if D>0: 
            root1 = (-b + sqrt(D)) / (2*a)
            root2 = (-b - sqrt(D)) / (2*a)
            root = (root1, root2)
            print("The 2 real roots are: %f, %f" %(root1, root2))
        elif D == 0: 
            root = -b/(2*a)
            print(" The real root is: %f" %root)
        else: print("The quadratic has no real roots")
    
