

class Central(object):
    
    def __init__(self, f, h =10E-5):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return( (f(x+h)-f(x-h))/(2*h) )

def sympy_calc(f, x):
    import sympy
    df_expr = sympy.diff(f)
    df = sympy.lambdify([sympy.Symbol('x')], df_expr)
    return(df(x))


def table(f, x, h=1E-5):
        import sympy
        x_list = x
        f_expr = f

        f = sympy.lambdify([sympy.Symbol('x')],f)
        df = Central(f)
        
        print("%-10s" %"x" + "%-20s" %"df(x)" + "%-10s" %"error")
        for x in x_list:
            print("%-10s" %x, end="")
            print("%-20s" %df(x), end="")
            print("%-10s" %(sympy_calc(f_expr, x) - df(x)))
    

def test_Central():
    from numpy import isclose
    def f(x):
        return(5*x**2 + 10*x + 20)
    df = Central(f, h=10E-9)
    x = 1
    expected = 20
    msg = "Diff value %f is not equal to expected value %f at x=%f" %(df(x), expected, x)
    assert isclose(df(x), expected), msg
    
if __name__ == "__main__":
    test_Central()


# Test code in other Python file
# import Central
# import sympy
# from math import sin


# def f(x):
#     return 0.25*x**4 + 10*x

# diff = Central.Central(f, h=10E-4)
# x = 2
# print ("df(%g)=%g" % (x, diff(x)))
# print ("exact:", x**3 + 10)


# # Sympy function part c/
# f_expr = "x*sin(2*x)"
# x = sympy.Symbol('x')
# f = sympy.lambdify([sympy.Symbol('x')],f_expr)

# x_list = (0,1,2,3,4,5,6)
# diff = Central.Central(f)
# print(diff(x=5))

# Central.table(f_expr, x_list)

