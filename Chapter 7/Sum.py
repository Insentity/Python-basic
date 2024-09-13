class Sum(object):

    def __init__(self, f, M, N):
        self.f = f
        self.M = M
        self.N = N

    # Return the result of sum
    def __call__(self, x):
        f = self.f
        M = self.M
        N = self.N
        
        temp = 0.0
        for i in range(M,N):
            k = i
            temp  += f(k,x)
        return(temp)

    # Return the value of a specific term in the sum
    def term(self, k, x):
        f = self.f
        return(f(k,x))
    

def test_Sum():
    from numpy import isclose
    def f(k, x):
        return (5*x**k + 10*x)

    S = Sum(f, M=0, N=5)
    x = 5
    expected = 4155
    msg = "Sum value %f is different from expected value %f" %(S(x), expected)
    assert isclose(S(x), expected) , msg

    expected = 675
    msg = "Term k=3 value %f is different from expected value %f" %(S.term(k=3, x=x), expected)
    assert isclose(S.term(k=3, x=x), expected), msg

if __name__ == "__main__":
    test_Sum()



# # Test on other Python file
# from Sum import Sum

# def term(k, x):
#     return ((-x)**k)

# S = Sum(term, M=0, N=3)
# x = 0.5
# k=3

# print(S(x))
# print(S.term(k=k, x=x))

# # Taylor expansion
# from math import sin, factorial, pi
# x_approx = pi+0.00001
# def term(k,x):
#     return ( (sin(x_approx + pi/4*k))/(factorial(k)) * (x-x_approx)**k )

# S = Sum(term, M=0, N=3)
# x = pi
# print(S(x))