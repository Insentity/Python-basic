"""
A module that  reads temperature in Fahrenheit from a file and convert to Celsius degree

Input:
Output:
"""
import os


# Main function
def Fahr2Cel():
    x = eval(get_input())
    return (x-32)*5/9

# Get input function
def get_input():
    try:
        folder_path = "C:\CongLuan\Courses\Python basics\Exercises\Python-basic\Chapter 4"
        abs_path = os.path.join(folder_path, "Exercise_4.3.txt")
        with open(abs_path, 'r') as infile:
            count = 0
            for line in infile:
                if count == 2: data = line.split()
                count += 1
        x = data[2]
    except ValueError:
        print("Error")
        sys.exit(1)
    return x


# Test function
def test_Fahr2Cel():
    x = 32
    result_expected = 0
    eps = 1E-5  # Tolerance
    result = Fahr2Cel(x)
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
