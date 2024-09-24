class Ellipse(object):
    def __init__(self, x0, y0, a, b):
        self.x0, self.y0, self.a, self.b = x0, y0, a, b

    def area(self):
        from math import pi
        return pi*self.a*self.b

    def circumference(self):
        from math import sqrt, pi
        return 2*pi*sqrt((self.a**2 + self.b**2)/2)
    
class Circle(Ellipse):
    def __init__(self, x0, y0, a):
        Ellipse.__init__(self, x0, y0, a, b=a)

