"""
A module that  reads temperature in Fahrenheit from a file and convert to Celsius degree

Input:
Output:
"""
import os
import numpy as np

folder_path = "C:\CongLuan\Courses\Python basics\Exercises\Python-basic\Chapter 4"  # Define path to folder containing the data file and python file
abs_path_input = os.path.join(folder_path, "Exercise_4.4.txt")    # Define path to the data file
abs_path_output = os.path.join(folder_path, "Exercise_4.4_output")

# Main function
def Fahr2Cel():
    Fahr = np.array(get_input(), dtype= float)    # Convert string list into float list
    Cel = [(temperature-32)*5/9 for temperature in Fahr]    # Calculate Celsius temperature from Fahrenheit
    outfile = open(abs_path_output, "w")       # Create and open output text file
    outfile.write("%10s   " %"Fahrenheit")      # Write the first row. %10s means 10 string character
    outfile.write("%10s   \n" %"Celsius")       # Also 10 string character but Celsius is only 7. Thus the remaining 3 string characters will be whitespace
    for x in range(len(Fahr)):
        outfile.write("%10.4f   " %Fahr[x])     #10 float characters with 4 numbers after decimal point
        outfile.write("%10.4f   \n" %Cel[x])
    return Fahr, Cel

# Get input function
def get_input():
    try:
        
        infile = open(abs_path_input, 'r')    # Open the data file
        lines = infile.readlines()  # Read all lines in the data file and store in "lines" variable
        result = []
        for x in range(3,9):    # Read only the lines that contain temperature values
            result.append(lines[x].split()[2])

    except ValueError:
        print("Error")
        sys.exit(1)
    return result   # Return string of Fahrenheit values


# Test function
def test_Fahr2Cel():
    result_expected = 31
    eps = 1E-5  # Tolerance
    result = Fahr2Cel()
    success = abs(result[1][5] - result_expected) < eps
    assert success, "Found result = %g not %g" %(result, result_expected)

# Test block
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "test":
        test_Fahr2Cel()
    else:
        result = Fahr2Cel()
        print(result)
