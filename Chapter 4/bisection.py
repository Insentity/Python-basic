# Main function
def bisection(f, a, b, eps):
    fa = f(a)
    if fa*f(b) > 0:
        return None, 0

    i = 0   # iteration counter
    while b-a > eps:
        i += 1
        m = (a + b)/2.0
        fm = f(m)
        if fa*fm <= 0:
            b = m  # root is in left half of [a,b]
        else:
            a = m  # root is in right half of [a,b]
            fa = fm
    return m, i

# Upgrade of main function
def bisection_evolution(f, a, b, eps):
    """As bisection, but return list of (current interval, current root)."""
    fa = f(a)
    if fa*f(b) > 0:
        return None

    result = []
    while b-a > eps:
        m = (a + b)/2.0
        result.append(([a, b], m))
        fm = f(m)
        if fa*fm <= 0:
            b = m  # root is in left half of [a,b]
        else:
            a = m  # root is in right half of [a,b]
            fa = fm
    return result

# Test function for bisection()
def test_bisection():
    def f(x):
        return 2*x - 3   # one root x=1.5

    eps = 1E-5
    x_expected = 1.7
    x, iter = bisection(f, a=0, b=10, eps=eps)
    success = abs(x - x_expected) < eps  # test within eps tolerance
    assert success, 'found x=%g != %g' % (x, x_expected)

# Get input function
def get_input():
    """Get f, a, b, eps from the command line."""
    from scitools import StringFunction
    try:
        f = StringFunction.StringFunction(sys.argv[1])
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        eps = float(sys.argv[4])
    except IndexError:
        print('Usage %s: f a b eps' % sys.argv[0])
        sys.exit(1)
    return f, a, b, eps


# Test block for bisection()
# If this bisection.py file is executed here, then __name__ = main. Then the test block is executed
# Else if bisection.py is imported (as a module) by another file, __name__ = 'bisection'
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':    # Runs test function if first command-line argument is 'test'
        print(sys.argv[1])
        test_bisection()
    else:
        f, a, b, eps = get_input()  #Else we run the bisection function with input data from command line
        x, iter = bisection(f, a, b, eps)
        print ('Found root x=%g in %d iterations' % (x, iter))

# Command line example: python bisection.py "x - (x-1)*sin(x)" -2 1 0.0001