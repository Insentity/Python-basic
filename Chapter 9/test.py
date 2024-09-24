from Sine12 import *

a = Sine1()
b = Sine2()

print("%g %g %g" %(a(5), a.df(5), a.ddf(5)))
print("%g %g %g" %(b(5), b.df(5), b.ddf(5)))