import numpy as np

a = 5
x = np.random.randint(0, 20, size =1000000)
y = np.random.randint(0, 20, size =1000000)

@profile
def axpy1(a,x,y):
    r = a*x + y
    return r
axpy1(a,x,y)


r = np.zeros(1000000)
@profile
def axpy2(a,x,y,r):
    r[:] = x
    r *= a
    r += y
    return r

axpy2(a,x,y,r)

# Memory check: python -m memory_profiler "D:\vgu\Post-graduate courses\Python\Python files\Exercises\Python-basic\Chapter 5\Test.py"\Python\Python files\Exercises\Python-basic>
# CPU time check: kernprof -l -v "D:\vgu\Post-graduate courses\Python\Python files\Exercises\Python-basic\Chapter 5\Test.py"