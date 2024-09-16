class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients


    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s


    def __add__(self, other):
        """Return self + other as Polynomial object."""
        # Two cases:
        #
        # self: X X X X X X X
        # other: X X X
        #
        # or:
        #
        # self: X X X X X
        # other: X X X X X X X X
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:] # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)
    

class Parabola(Polynomial):
    def __init__(self, c0, c1, c2):
        Polynomial.__init__(self, [c0, c1, c2])

class Line(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)