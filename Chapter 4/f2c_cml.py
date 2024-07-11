"""
A module that  computes temperature in Celsius degree from Fahrenheit using input from command line

Input:
Output:
"""

# Main function
def Fahr2Cel():
    x = get_input()
    if x == "test": x=32
    else: x = eval(x)
    return (x-32)*5/9

# Get input function
def get_input():
    try:
        x = sys.argv[1]
    except ValueError:
        print("Error")
        sys.exit(1)
    return x


# Test function
def test_Fahr2Cel():
    x = 32
    result_expected = 0
    eps = 1E-5  # Tolerance
    result = Fahr2Cel()
    success = abs(result - result_expected) < eps
    assert success, "Found result = %g not %g" %(result, result_expected)
    print("%g Fahrenheit is %g Celsius degree" %(x, result))

# Test block
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        test_Fahr2Cel()
    else:
        result = Fahr2Cel()
        print(result)


# Example command line: 
# python "C:\\CongLuan\\Courses\\Python basics\\Exercises\\Python-basic\\Chapter 4\\f2c_cml.py" test
# python "C:\\CongLuan\\Courses\\Python basics\\Exercises\\Python-basic\\Chapter 4\\f2c_cml.py" 36