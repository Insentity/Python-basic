class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)


class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h
    

from math import sin, pi
a = Forward1(Forward1(sin))
print(Forward1(sin))
print(a)
print(a(5))